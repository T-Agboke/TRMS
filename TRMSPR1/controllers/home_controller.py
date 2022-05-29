# For request not pertaining to specific class

def route(app):
    @app.route("/")
    def hello():
        return "Hello, World!"