from exceptions.resource_not_found import ResourceNotFound
from models.employees import Employees
from repositories import employee_repo
from util.db_connection import connection

# def _build_request(record):

class EmployeesRepoImpl(employee_repo):

    def _build_employee(record):
        return Employees(e_id=(record[0]), d_id=(record[1]), e_firstname=(record[2]),
                         e_lastname=(record[3]), email=(record[4]), pwd=(record[5]))

#     def employee_login(self, e_id):
#         user = raw_input("Username: ")
#         passw = raw_input("Password: ")
#         f = open("users.txt", "r")
#         for line in f.readlines():
#             us, pw = line.strip().split("|")
#             if (user in us) and (passw in pw):
#                 print
#                 "Login successful!"
#                 return True
#         print
#         "Wrong username/password"
#         return False
#
#
# return _build_employee()
# def login():
#     user = raw_input("Username: ")
#     passw = raw_input("Password: ")
#     f = open("users.txt", "r")
#     for line in f.readlines():
#         us, pw = line.strip().split("|")
#         if (user in us) and (passw in pw):
#             print "Login successful!"
#             return True
#     print "Wrong username/password"
#     return False
