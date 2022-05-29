class Employees:
    def __init__(self, e_id, d_id, e_firstname, e_lastname, email, pwd):
        self.e_id = e_id
        self.d_id = d_id
        self.e_firstname = e_firstname
        self.e_lastname = e_lastname
        self.email = email
        self.pwd = pwd


    def __repr__(self):
        return str({
            'e_id': self.e_id,
            'd_id': self.d_id,
            'e_firstname': self.e_firstname,
            'e_lastname': self.e_lastname,
            'email': self.email,
            'pwd': self.pwd,

        })

    def json(self):
        return {
            'e_id': self.e_id,
            'd_id': self.d_id,
            'e_firstname': self.e_firstname,
            'e_lastname': self.e_lastname,
            'email': self.email,
            'pwd': self.pwd,

        }

