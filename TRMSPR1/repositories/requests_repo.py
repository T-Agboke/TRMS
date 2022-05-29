from abc import ABC, abstractmethod


class RequestsRepo(ABC):
    pass

    @abstractmethod
    def create_request(self, request):
        pass

    @abstractmethod
    def get_request(self, request_id):
        pass

    @abstractmethod
    def all_requests(self):
        pass

    @abstractmethod
    def update_request(self, change):
        pass

    @abstractmethod
    def delete_request(self, request_id):
        pass

    @abstractmethod
    def approve_request (self, request_id):
        pass

    @abstractmethod
    def deny_request(self, request_id):
        pass
    # request has been denied, contact dircts

    # @abstractmethod
    # def auto_approve_req (self, request_id)