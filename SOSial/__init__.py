from flask import Flask, jsonify, request, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.secret_key = "password"

# SQLAlchemy Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

db = SQLAlchemy(app)

# Session Configuration
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SECURE"] = False  # TODO: On production set to True
# PERMANENT_SESSION_LIFETIME  # TODO: Set value on production
app.config["SESSION_TYPE"] = "sqlalchemy"
# SESSION_PERMANENT # TODO: On production set to False
app.config["SESSION_USE_SIGNER"] = True
app.config["SESSION_SQLALCHEMY"] = db
app.config["SESSION_SQLALCHEMY_TABLE"] = "Session"


api = Api(app)
session = Session(app)
ma = Marshmallow(app)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/test", methods=["GET", "POST"])
def test():
    response = {"response": "success"}
    if request.method == "POST":
        json_data = request.get_json()
        response["message"] = json_data["message"]
    return jsonify(response), 200


from SOSial.Resources.login import UserLogin

api.add_resource(UserLogin, "/login")

from SOSial.Resources.register import UserRegister

api.add_resource(UserRegister, "/register")

from SOSial.Resources.profile import UserProfile

api.add_resource(UserProfile, "/<string:username>")

from SOSial.Resources.logout import UserLogout

api.add_resource(UserLogout, "/logout")

from SOSial.Resources.location import UserLocation

api.add_resource(UserLocation, "/location")

from SOSial.Resources.family import UserFamily

api.add_resource(UserFamily, "/family")