from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, what a great World!</p>"

@app.route("/<name>")
def user(name):   
    return "Hello "+ name + "!"


if __name__ == "__main__":
    app.run(debug=True, port=8081)