class Requests:
    def __init__(self, req_id, event_id, status, grade, req_type, reimb_amount):
        self.req_id = req_id
        self.event_id = event_id
        self.status = status
        self.grade = grade
        self.req_type = req_type
        self.reimb_amount = reimb_amount

# -----------------------------------------------------------------------

    def __repr__(self):
        return str({
            'req_id': self.req_id,
            'event_id': self.event_id,
            'status': self.status,
            'grade': self.grade,
            'req_type': self.req_type,
            'reimb_amount': self.reimb_amount

        })

# -----------------------------------------------------------------------

    def json(self):
        return {
            'req_id': self.req_id,
            'event_id': self.event_id,
            'status': self.status,
            'grade': self.grade,
            'req_type': self.req_type,
            'reimb_amount': self.reimb_amount

        }