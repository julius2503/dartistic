from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import helper
import os

app = Flask(__name__)

# DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

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
#

@app.route("/", methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        username = request.form['username']
        if username != "" or username != " " or username != "db":
            new_user = User(
                name = username
            )
            db.session.add(new_user)
            db.session.commit()
            print("Added new User: " + username)
    users = User.query.order_by(User.created_at).all()
    return render_template("index.html", users=users)

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
                value = helper.getValue(valueOne) + helper.getValue(valueTwo) + helper.getValue(valueThree)
            )
            db.session.add(new_throw)
            db.session.commit()
            print("Submitted")
        print(" ")
    darts = Throw.query.order_by(Throw.time)
    dartsFromUser = Throw.query.filter(Throw.user == name)
    avg = helper.getAvg(dartsFromUser)
    overallScore = helper.getScore(dartsFromUser)
    return render_template("user.html", name=name, darts = darts, avg=avg, score=overallScore)




@app.route("/<name>/history")
def history(name):   
    return render_template("history.html", name=name)

@app.route("/<name>/statistics")
def stats(name):   
    return render_template("statistics.html", name=name)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8081))
    app.run(debug=True, host='0.0.0.0', port=port)