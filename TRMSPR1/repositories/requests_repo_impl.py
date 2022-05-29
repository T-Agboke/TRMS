from exceptions.resource_not_found import ResourceNotFound
from models.requests import Requests
from repositories.requests_repo import RequestsRepo
from util.db_connection import connection


def _build_request(record):
    return Requests(req_id=(record[0]), event_id=(record[1]), status=(record[2]),
                    grade=(record[3]), req_type=(record[4]), reimb_amount=(record[5]))


class RequestsRepoImpl(RequestsRepo):

# CREATE--------------------------------------
    def create_request(self, request):
        sql = "INSERT INTO requests VALUES (DEFAULT,NULL,%s,%s,%s,%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [request.status, request.grade, request.req_type, request.reimb_amount])

        connection.commit()
        record = cursor.fetchone()

        return _build_request(record)

    # READ REQUESTS--------------------------------
    def get_request(self, req_id):
        sql = "SELECT * from requests WHERE req_id = %s"
        cursor = connection.cursor()

        cursor.execute(sql, [req_id])

        record = cursor.fetchone()
        # record as an object to retrieve return from cursor

        if record:
            return _build_request(record)
        else:
            raise ResourceNotFound(f"Request with id: {req_id} -Not Found")

    def all_requests(self):
        sql = "SELECT * FROM requests"
        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        requests_list = []

        for record in records:
            request = _build_request(record)
            requests_list.append(request)

        return requests_list

    # UPDATE REQUEST--------------------------------

    def update_request(self, change):

        sql = "UPDATE requests SET event_id=%s, status=%s, grade=%s, req_type=%s, reimb_amount=%s " \
              "WHERE req_id = %s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.event_id, change.status, change.grade, change.req_type, change.reimb_amount,
                       change.req_id])

        connection.commit()
        record = cursor.fetchone()

        return _build_request(record)


    # DELETE REQUEST--------------------------------

    def delete_request(self, req_id):

        sql = "DELETE FROM requests WHERE req_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [req_id])
        connection.commit()

    def approve_request(self, req_id):
        pass

    def deny_request(self, req_id):
        pass
#-------------------------------------------

# TESTS-------------------------------------------

def _test():
    print("-------GET--------")
    # GET all requests test
    rr = RequestsRepoImpl()
    request = rr.get_request(1)
    print(request)
    print(rr.all_requests())
    print("------CREATE------")

    # CREATE new request test
    request = Requests(req_id=0, event_id=0, status="approv_pending", grade="pass", req_type="full_reimb", reimb_amount=750)
    print(rr.create_request(request))
    print(rr.all_requests())
    print("-----UPDATE-----")


    # UPDATE request test
    request.status = "approved"
    request = rr.update_request(request)
    print(request)
    print("------DELETE-----")


    # DELETE request test
    print("DELETE REQUEST")
    rr.delete_request(request.req_id)
    print(rr.all_requests())
    print(rr.get_request(request.req_id))





if __name__ == '__main__':
    _test()