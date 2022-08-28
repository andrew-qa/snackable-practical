## Snackable Practical Task

# Implemented items

- Build a single API that serves all file and segment metadata when given a “fileId” as an
input parameter.
  1. Only show “FINISHED” files in your API
  2. Requested files that are “PROCESSING” or “FAILED” should return an exception
- Create a storage mechanism to reduce the HTTP overhead of making API calls
  1. Include an ingestion procedure that will only save “FINISHED” files
  2. Build a polling procedure that will continually check files marked as
“PROCESSING” and save them once they are marked “FINISHED”

# How to Run

This is python application, so `python3` should be installed on the machine in order to run app. 
Then execute following commands to install dependencies and run app:
```
pip3 install -r requirements.txt
make run
```
Application will be available on http://127.0.0.1:5000/

# API endpoints

- `/api/all` - same as http://interview-api.snackable.ai/api/file/all
- `/api/details/<string:id>` - get file by id with details and segments

And that's it for now. Have a nice day :-)
