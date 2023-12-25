import flask

app = flask.Flask(__name__)

# DB

@app.route("/")
def hello_world():
    return flask.render_template("index.html")

@app.route("/<name>")
def user(name):   
    return flask.render_template("user.html", name=name, average = 120)

@app.route("/<name>/history")
def history(name):   
    return name + " your last throws are listed here"

@app.route("/<name>/statistics")
def stats(name):   
    return name + " your stats are listed here"


if __name__ == "__main__":
    app.run(debug=True, port=8081)