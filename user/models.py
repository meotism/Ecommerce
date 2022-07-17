from flask import Flask, jsonify, redirect, request, session
from config.db import MongoDB
import json
import uuid
from passlib.hash import pbkdf2_sha256
import datetime
collection_name = 'user'

mongoDB = MongoDB()

class User:
  def __init__(self):
    self.collection = mongoDB.get_db().get_collection(collection_name)

  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200

  def signup(self):
    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('name'),
      "email": request.form.get('email'),
      "password": request.form.get('password'),
      "phonenumber": request.form.get('phonenumber'),
      "ammount":0,
      "modified_date": datetime.datetime.now(),
    }

    # Encrypt the password
    user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Check for existing email address
    if self.collection.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    if self.collection.insert_one(user):
      return self.start_session(user)
    return jsonify({ "error": "Signup failed" }), 400
  
  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):
    # find user by email or phone number
    user = self.collection.find_one({ "$or":[{"email": request.form.get('name')},{"phonenumber": request.form.get('name')}]})
    print(user)
    print(request.form.get('password'))
    #user = mongoDB.self.collection.find({ "$or":[{"email": request.form.get('login')},{"phonenumber": request.form.get('login')}]})
    if (user) and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
      return self.start_session(user)
    
    return jsonify({ "error": "Login failed" }), 401

  def update_user(user_id, self):
    user = {
      "name": request.form.get('name'),
      "email": request.form.get('email'),
      "phonenumber": request.form.get('phonenumber'),
      "ammount":request.form.get('ammount'),
      "modified_date": datetime.datetime.now(),
    }
    if self.collection.update_one({'_id': user_id}, {'$set': user}):
      return jsonify(user), 200