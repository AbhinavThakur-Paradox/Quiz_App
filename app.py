from flask import *
from flask_sqlalchemy import*

#app set-up
app = Flask(__name__)

# datbase set-up
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#admin table
class Admin(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    password = db.Column(db.String(16), nullable = False)

#user table
class User(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    password = db.Column(db.String(16), nullable = False)

#login route
@app.route("/", methods = ["POST", "GET"])
def login() :
    if request.method == "POST" :
        return redirect("/admin_login")
    return render_template("login.html")

#admin login page
@app.route("/admin_login")
def admin_login() :
    return render_template("admin_login.html")

if __name__ == "__main__" :
    app.run(debug = True)