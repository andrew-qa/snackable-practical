## Snackable Practical Task

# Implemented items

- Build a single API that serves all file and segment metadata when given a “fileId” as an
input parameter.
a. Only show “FINISHED” files in your API
b. Requested files that are “PROCESSING” or “FAILED” should return an exception
- Create a storage mechanism to reduce the HTTP overhead of making API calls
a. Include an ingestion procedure that will only save “FINISHED” files
b. Build a polling procedure that will continually check files marked as
“PROCESSING” and save them once they are marked “FINISHED”

# How to Run

This is python application, so `python3` should be installed on the machine in order to run app. 
Then execute following command to install dependencies and run app:
```
pip3 install -r requirements.txt
make run
```