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
    if request.method == "GET" :
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username = username).first()
        if user:
            if user.password == password:
                pass
    return render_template("login.html")

#admin login page
@app.route("/admin_login", methods = ["POST", "GET"])
def admin_login() :
    if request.method == "POST" :
        username = request.form.get("username")
        password = request.form.get("password")
        admin = Admin.query.filter_by(username = username).first()
        if admin:
            if admin.password == password:
                print("Admin logged in")
                return redirect("/admin_dashboard")
            else :
                pass
        else :
            pass
    return render_template("admin_login.html")

#admin dashboard
@app.route("/admin_dashboard")
def admin_dashboard() :
    return render_template("admin_dashboard.html")

@app.route("/admin_dashboard/add_user", methods = ["POST", "GET"])
def add_user():
    if request.method == "POST" :
        username = request.form.get("userName")
        first = request.form.get("firstName")
        last = request.form.get("lastName")
        password = request.form.get("password")

        if not User.query.filter_by(username = username).first() : 
            newUser = User(username = username, firstNme = first, lastName = last, password = password)
            db.session.add(newUser)
            db.session.commit()
            return render_template("add_user.html", message = "User added successfully")
        else :
            return render_template("add_user.html", message = "Username already exists")
        return render_temlate("add_user.html")

if __name__ == "__main__" :
    app.run(debug = True)