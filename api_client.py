import requests

class InterviewAPI:
    def __init__(self):
        self.base_url = "http://interview-api.snackable.ai/api/"

    def all_files(self):
        url = self.base_url + 'file/all'
        return requests.get(url).json()

    def file_by_id(self, id):
        url = self.base_url + 'file/details/' + id
        return requests.get(url).json()

    def segments_by_id(self, id):
        url = self.base_url + 'file/segments/' + id
        return requests.get(url).json()