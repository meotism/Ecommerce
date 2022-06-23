# from dotenv import load_dotenv
from functools import wraps
from api import api_blueprint
from flask import Flask, redirect, render_template, session, url_for
from datetime import datetime
from flask_cors import CORS
from config.db import MongoDB
from user.routes import user_blueprint

mongodB=MongoDB()
# Routes
from user import routes
app = Flask(__name__)
app = Flask(__name__, static_folder = './assets')
app.secret_key = 'super secret key'
# CORS(app, resources={r"/api/*": {"origins": "*"}})
# load_dotenv(dotenv_path='.env')


app.register_blueprint(user_blueprint, url_prefix='/user')

# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap

@app.route('/')
def login():
    return render_template('login.html')
@app.route('/login')
def loginpage():
    return render_template('login.html')

@app.route('/home')
def home():
    #render index.html
    return render_template('index.html')
@app.route('/home1')
def home1():
    #render index.html
    return render_template('index_2.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')