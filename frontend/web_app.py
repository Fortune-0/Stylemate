from flask import Flask, render_template, url_for

web_app = Flask(__name__)

@web_app.route("/", strict_slashes=False)
def serve_home_page():
    """Render home page to browser"""
    print(url_for('static', filename="2-stylemate.html"))
    return(render_template("1-stylemate.html"))
@web_app.route("/getoutfit", strict_slashes=False)
def serve_get_outfit_page():
    """Render get outfit  page to browser"""
    return(render_template("2-stylemate.html"))
@web_app.route("/getdescribe", strict_slashes=False)
def serve_get_describe_page():
    """Render describe wardrobe page to browser"""
    return(render_template("3-stylemate.html"))

if __name__ == "__main__":
    web_app.run("0.0.0.0", port=5001)
