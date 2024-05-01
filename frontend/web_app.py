from flask import Flask, render_template

web_app = Flask(__name__)

@web_app.route("/", strict_slashes=False)
def serve_home_page():
    """Render home page to browser"""
    return(render_template("1-stylemate.html"))

if __name__ == "__main__":
    web_app.run("0.0.0.0", port=5001)
