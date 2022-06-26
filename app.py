# from dotenv import load_dotenv
from functools import wraps
from api import api_blueprint
from flask import Flask, redirect, render_template, request, session, url_for
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
    return render_template('index_2.html')
@app.route('/login')
def loginpage():
    return render_template('login.html')

@app.route('/home')
def home():
    # check session for logged in user
    if 'logged_in' in session:
      return render_template('index_2.html')
    else:
      return redirect(url_for('login'))
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/product/apple')
def apple():
    return render_template('single-product.html')
@app.route('/single-news')
def single_news():
    return render_template('single-news.html')
@app.route('/news')
def news():
    return render_template('news.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/cart')
def cart():
    return render_template('cart.html')
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')
@app.route('/404')
def error():
    return render_template('404.html')
@app.route('/shop')
def shop():
    return render_template('shop.html')