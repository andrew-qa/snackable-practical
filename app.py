from flask import Flask, request, jsonify
import requests
import api_client

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, API!</p>"

@app.route("/api/all", methods=["GET"])
def get_all():
    client = api_client.InterviewAPI()
    return client.all_files()

@app.route("/api/details/<string:id>", methods=["GET"])
def get_file_details(id):
  client = api_client.InterviewAPI()

  file_details = client.file_by_id(id)
  if file_details is None:
    return jsonify({"error": f"File with {id} and status FINISHED can\'t be found"}), 404

  file_segments = client.segments_by_id(id)

  file_details['segments'] = file_segments

  return file_details
