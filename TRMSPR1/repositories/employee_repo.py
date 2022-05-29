from abc import abstractmethod, ABC


class EmployeeRepo(ABC):
    pass

@abstractmethod
def employee_login(self, e_id):
    pass


