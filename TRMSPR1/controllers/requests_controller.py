from exceptions.resource_not_found import ResourceNotFound
from repositories.requests_repo_impl import RequestsRepoImpl
from services.requests_service import RequestsOperations
from flask import request
from models.requests import Requests


rr = RequestsRepoImpl()
ro = RequestsOperations(rr)

#----------------------------------------------------------

def route(app): # GET all requests
    @app.route("/requests", methods=['GET'])
    def get_all_requests():
        return repr(ro.get_all_requests())

#GET requests by ID

    @app.route("/requests/<req_id>", methods=['GET'])
    def get_request(req_id):
        try:
            return repr(ro.get_request_by_id(req_id)), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404
# ---------------------------------------------------------
# POST new request

    @app.route("/requests", methods=["POST"])
    def post_request():
        body = request.json
        requests = Requests(req_id=body["reqId"], event_id=body["eventId"], status=body["status"], grade=body["grade"],
                            req_type=body["reqType"], reimb_amount=body["reimbAmount"])

        requests = ro.create_request(requests)

        return repr(requests), 200
# PUT CLIENT (update)-----------------------------

    @app.route("/requests/<req_id>", methods=["PUT"])
    def put_request(req_id):
        body = request.json
        requests = Requests(req_id=body["reqId"], event_id=body["eventId"], status=body["status"], grade=body["grade"],
                            req_type=body["reqType"], reimb_amount=body["reimbAmount"])
        requests = ro.update_request(requests)
        return requests.json(), 201

# ----------------------------------------------
# DELETE
    @app.route("/requests/<req_id>", methods=["DELETE"])
    def del_request(req_id):
        ro.delete_request(req_id)
        return '', 204 #No Content
# ----------------------------------------------
# APPROVE REQUEST
# ----------------------------------------------
# DENY REQUEST