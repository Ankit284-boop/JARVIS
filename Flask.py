

# from flask import Blueprint, flash, redirect, request, url_for
# from flask import Flask,render_template,jsonify
# app = Flask(__name__)

# # @app.route('/')
# # def hello_world():
# @app.route('/about')
# def harry1():
#     return render_template("404.html")


# @app.route('/')
# def harry():
#     return render_template("index.html")
# @app.errorhandler(404)
# def invalid_route(e):
#     return redirect(url_for('harry1'))
#     # return render_template('index.html')
#     # return jsonify({'errorCode': 404, 'message': 'Route not found'})

# #     #return "Invalid route."
# app.version =1.0
from flask import Flask, render_template, request, redirect, jsonify, abort, g, url_for, session
import re
import MySQLdb.cursors
from flask_mysqldb import MySQL
from datetime import datetime
import json
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
import warnings
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from passlib.hash import sha256_crypt
# mysql+pymysql://username:password@localhost/databasename
engine = create_engine("mysql+pymysql://shubham:shubham123@localhost/register")
db1 = scoped_session(sessionmaker(bind=engine))
app = Flask(__name__)

# app.static_folder = 'static'
# register form
# @app.route("/register",methods=["GET","POST"])
# def register():
# 	if request.method=="POST":
# 		name=request.form.get("name")
# 		username=request.form.get("username")
# 		password=request.form.get("password")
# 		confirm=request.form.get("confirm")
# 		secure_password=sha256_crypt.encrypt(str(password))

# 		usernamedata=db1.execute("SELECT username FROM users WHERE username=:username",{"username":username}).fetchone()
# 		#usernamedata=str(usernamedata)
# 		if usernamedata==None:
# 			if password==confirm:
# 				db1.execute("INSERT INTO users(name,username,password) VALUES(:name,:username,:password)",
# 					{"name":name,"username":username,"password":secure_password})
# 				db1.commit()
# 				flash("You are registered and can now login","success")
# 				return redirect(url_for('login'))
# 			else:
# 				flash("password does not match","danger")
# 				return render_template('register.html')
# 		else:
# 			flash("user already existed, please login or contact admin","danger")
# 			return redirect(url_for('login'))

# 	return render_template('register.html')


@app.route("/login.php")
def loginyu():
    return render_template('login.php')


def fxn():
    warnings.warn("deprecated", DeprecationWarning)


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()
warnings.filterwarnings("ignore")

# app.run(debug=True)
# @app.errorhandler(404)
# def resource_not_found(e):
#     return jsonify(error=str(e)), 404

# @app.route("/cheese")
# def get_one_cheese():
#     resource = get_resource()

#     if resource is None:
#         abort(404, description="Resource not found")

#     return jsonify(resource)
# app.secret_key ='password'

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)
mail = Mail(app)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)
app.secret_key = 'ankit'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contacts'
mysql = MySQL(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)


class login(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(12), nullable=False)


# class Posts(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     slug = db.Column(db.String(21), nullable=False)
#     content = db.Column(db.String(120), nullable=False)
#     date = db.Column(db.String(12), nullable=True)
#     img_file = db.Column(db.String(12), nullable=True)
@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.php')


@app.route("/config.php")
def loginuserphp():
    return render_template('config.php')


@app.errorhandler(404)
def resource_not_found(e):
    return render_template('404.html')


@app.route("/registerbyname")
def cookie():
    return render_template('name.html', params=params)


@app.route("/detectos")
def ANKITSAT():
    return render_template('ER.HTML', params=params)


@app.route("/")
def home():

    return render_template('index.html', params=params)


@app.route("/about")
def about():
    return render_template('about.html', params=params)


@app.route("/form")
def form():
    return render_template('contact.html', params=params)


@app.route("/dfg")
def contactus():
    return render_template('redirect.html', params=params)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if(request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num=phone,
                         msg=message, date=datetime.now(), email=email)
        db.session.add(entry)
        db.session.commit()
        a = db.session.add(entry)
        # if(a):
        #     @app.route("/contact")
        #     def df():
        #         return redirect(url_for('form'))
        # else:
        #     @app.errorhandler(404)
        #     def invalid_route(e):
        #     return redirect(url_for('harry123'))

        # mail.send_message('New message from ' + name,
        #                   sender=email,
        #                   recipients=[params['gmail-user']],
        #                   body=message + "\n" + phone+"\n"+email
        #                   )
        # from twilio.rest import Client
        # account = "AC5bce7dc5ca120e43b79330e4c631ebd9"
        # token = "6404067cbb193bf2208b2f6e5353e7a2"

        # client = Client(account, token)
        # a=("THANKS FOR CONTACTING US",name)

        # message = client.messages.create(to="+919330785851", from_="+19705502651",
        #                                  body="NEW MESSAGE,CHECK MAIL FIRST")

    import smtplib
    gmailaddress = ("satpatiankit@gmail.com ")
    gmailpassword = ("ankitsat@12345 ")
    mailto = (email)
    msg = ("GOOD BOY ")
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.starttls()
    mailServer.login(gmailaddress, gmailpassword)
    mailServer.sendmail(gmailaddress, mailto, msg)
    # print(" \n Sent!")
    mailServer.quit()
    return render_template('submit.html', params=params)

    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# reader = open('records.txt')
# try:
#     reader.write(f{name},{email},{message})
# finally:
#     reader.close()
# a = str(587)
# with open('dog_breeds.txt', 'w') as reader:
#     reader.write(a)

@app.route("/d")
def d():
    return render_template('offline.html')


# @app.route("/l" methods=["GET", "POST"])
@app.route("/register.php", methods=['GET', 'POST'])
def df():
    return render_template('register.php')


@app.route("/pug")
def pug():
    return render_template('redirect.html')


@app.route("/sd")
def r():
    return render_template('redirect1.html')
@app.route("/dashboard")
def route():
    return render_template('dashboard.html')    


@app.route("/dash", methods=['GET', 'POST'])
def dashboard():
    if ('user' in session and session['user'] == params['admin_user']):
        return render_template("index.html")

    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('pass')
        if username == params['admin_user'] and password == params['admin_password']:
            return render_template('blocker.html')
    else:
        redirect(url_for("/"))
   

app.run(debug=True)
