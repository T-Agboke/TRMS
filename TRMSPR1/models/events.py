class Events:
    def __init__(self, event_id, coverage, event_name):
        self.event_id = event_id
        self.coverage = coverage
        self.event_name = event_name

# -----------------------------------------------------------------------
    def __repr__(self):
        return str({
            'event_id':
            'coverage'
            'event_name'
        })

# -----------------------------------------------------------------------
    def json(self):
        return {
            'event_id':
            'coverage'
            'event_name'
        }
