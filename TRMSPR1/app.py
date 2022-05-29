from flask import Flask
import controllers.front_controller as fc
from repositories.requests_repo_impl import RequestsRepoImpl
from services.requests_service import RequestsOperations

app = Flask(__name__)

rr = RequestsRepoImpl()
ro = RequestsOperations(rr)


@app.route("/")
def helllo():
    return "Hello World!"


# Establish all Flask routes
fc.route(app)


if __name__ == '__main__':
    app.run()

