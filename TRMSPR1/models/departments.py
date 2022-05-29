class Departments:
    def __init__(self, d_id, d_name, d_head, head_id):
        self.d_id = d_id
        self.d_name = d_name
        self.d_head = d_head
        self.head_id = head_id

# -----------------------------------------------------------------------

    def __repr__(self):
        return str({
            'd_id': self.d_id,
            'd_name': self.d_name,
            'd_head': self.d_head,
            'head_id': self.head_id
        })
# -----------------------------------------------------------------------

    def json(self):
        return {
            'd_id': self.d_id,
            'd_name': self.d_name,
            'd_head': self.d_head,
            'head_id': self.head_id
        }