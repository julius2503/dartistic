from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import helper

app = Flask(__name__)

# DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Throw(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(200))
    dartOne = db.Column(db.String(200))
    dartTwo = db.Column(db.String(200))
    dartThree = db.Column(db.String(200))
    value = db.Column(db.Integer)
    time = db.Column(db.DateTime(), default=datetime.utcnow)

app.app_context().push()
db.create_all()

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/<name>", methods=['GET', 'POST'])
def user(name):
    if request.method == 'POST':
        valueOne = request.form['first-dart']
        valueTwo = request.form['second-dart']
        valueThree = request.form['third-dart']
        print(" ")
        print(name + " threw: " + valueOne + ", " + valueTwo + ", " + valueThree)
        if helper.check(valueOne, valueTwo, valueThree) == True:
            new_throw = Throw(
                user = name,
                dartOne = valueOne,
                dartTwo = valueTwo,
                dartThree = valueThree,
                value = 0
            )
            db.session.add(new_throw)
            db.session.commit()
            print("Submitted")
        print(" ")
    return render_template("user.html", name=name)




@app.route("/<name>/history")
def history(name):   
    return render_template("history.html", name=name)

@app.route("/<name>/statistics")
def stats(name):   
    return render_template("statistics.html", name=name)


if __name__ == "__main__":
    app.run(debug=True, port=8081)