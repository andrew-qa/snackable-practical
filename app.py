from flask import Flask, request, jsonify
import requests
import api_client
import time
import threading
import os
import tempfile
import json

app = Flask(__name__)
temp_dir = tempfile.TemporaryDirectory()

@app.before_first_request
def before_first_request():
    def poll_status():
        client = api_client.InterviewAPI()
        print ("Temp dir: {}".format(temp_dir.name))
        while True:
            print("Starting task .....")
            all_files = client.all_files()
            for file in all_files:
                file_id = file['fileId']
                # “PROCESSING” or “FAILED” files will not be stored in the temporary directory.
                if not is_exists(os.path.join(temp_dir.name, file_id)):
                    print("Polling status for file: {}".format(file_id))
                    file_details = client.file_by_id(file_id)
                    file_segments = client.segments_by_id(file_id)
                    file_details['segments'] = file_segments
                    if file_details is not None:
                        save_file(os.path.join(temp_dir.name, file_id) , file_details)
            time.sleep(60) 

    thread = threading.Thread(target=poll_status)
    thread.start()

def save_file(filepath, data):
    with open(filepath, 'w') as outfile:
        print("Saving file: {}".format(filepath))
        json.dump(data, outfile)

def is_exists(filename):
    return os.path.exists(filename)

def is_finished(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data['processingStatus'] == 'FINISHED'

def load_file(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data
    

@app.route("/")
def hello_world():
    return "<p>Hello, API!</p>"

@app.route("/api/all", methods=["GET"])
def get_all():
    client = api_client.InterviewAPI()
    return client.all_files()

@app.route("/api/details/<string:id>", methods=["GET"])
def get_file_details(id):
  file_path = os.path.join(temp_dir.name, id)
  if is_exists(file_path):
    print("Responding from local cache: {}".format(id))  
    return load_file(file_path)
  
  print("Requsting details from API: {}".format(id))
  client = api_client.InterviewAPI()
  file_details = client.file_by_id(id)
  if file_details is None:
    return jsonify({"error": f"File with {id} and status FINISHED can\'t be found"}), 404

  file_segments = client.segments_by_id(id)

  file_details['segments'] = file_segments

  return file_details

if __name__ == '__main__':
    app.run(debug=True)