from controllers import requests_controller, home_controller

def route(app):

    home_controller.route(app)
    requests_controller.route(app)
