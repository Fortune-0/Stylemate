from flask import Flask

web_app = Flask(__name__)

@web_app.route("/", strict_slashes=False)
def serve_home_page():
    return 