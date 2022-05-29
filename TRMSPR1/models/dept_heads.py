class DeptHeads:
    def __init__(self, head_id, head_name):
        self.head_id = head_id
        self.head_name = head_name

# -----------------------------------------------------------------------

    def __repr__(self):
        return str({
            'head_id': self.head_id,
            'head_name': self.head_name
        })

# -----------------------------------------------------------------------

    def json(self):
        return {
            'head_id': self.head_id,
            'head_name': self.head_name
        }