
from flask import Blueprint
from user.models import User
from flask import Flask, jsonify, redirect, request, session

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/signup',methods=['POST'])
def signup():
  return User().signup()

@user_blueprint.route('/signout')
def signout():
  return User().signout()

@user_blueprint.route('/login', methods=['POST'])
def login():
  return User().login()