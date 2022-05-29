
from repositories.requests_repo import RequestsRepo
from abc import ABC
from models.requests import Requests

class RequestsOperations:

    def __init__(self, requests_repo: RequestsRepo):
        self.requests_repo = requests_repo

    def create_request(self, request):
        return self.requests_repo.create_request(request)

    def get_request_by_id(self, req_id):
        return self.requests_repo.get_request(req_id)

    def get_all_requests(self):
        return self.requests_repo.all_requests()

    def update_request(self, change):
        return self.requests_repo.update_request(change)

    def delete_request(self, req_id):
        return self.requests_repo.delete_request(req_id)

    def approve_request(self, req_id):
        return self.requests_repo.approve_request(req_id)

    def deny_request(self, req_id):
        return self.requests_repo.deny_request(req_id)

