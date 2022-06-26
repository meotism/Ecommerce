from flask import Flask, jsonify, redirect, request, session
from config.db import MongoDB
import json
import uuid
import datetime
collection_name = 'product'

mongoDB = MongoDB()

class Product:
  def __init__(self):
    self.collection = mongoDB.get_db().get_collection(collection_name)

def get_product(product_id):
    product = mongoDB.get_db().get_collection(collection_name).find_one({'_id': product_id})
def get_products():
    products = mongoDB.get_db().get_collection(collection_name).find()
    return products
def create_product(product):
    # Create the product object
    product = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('name'),
      "discount": request.form.get('discount'),
      "price":request.form.get('price'),
      "category":request.form.get('category'),
      "desc": request.form.get('email'),
      "image":request.form.get('image'),
      "modified_date": datetime.datetime.now(),
    }
    if mongoDB.get_db().get_collection(collection_name).insert_one(product):
        return jsonify(product), 200

def update_product(product_id, product):
    product = {
      "name": request.form.get('name'),
      "discount": request.form.get('discount'),
      "price":request.form.get('price'),
      "category":request.form.get('category'),
      "desc": request.form.get('email'),
      "image":request.form.get('image'),
      "modified_date": datetime.datetime.now(),
    }
    if mongoDB.get_db().get_collection(collection_name).update_one({'_id': product_id}, {'$set': product}):
        return jsonify(product), 200
    
def delete_product(product_id):
    if mongoDB.get_db().get_collection(collection_name).delete_one({'_id': product_id}):
        return jsonify({}), 200

def get_product_by_category(category):
    products = mongoDB.get_db().get_collection(collection_name).find({'category': category})
    return products

def get_product_by_name(name):
    products = mongoDB.get_db().get_collection(collection_name).find({'name': name})
    return products

#rank product by price
def rank_product_by_price(products):
    products.sort(key=lambda x: x['price'])
    return products
#reverse rank product by price
def reverse_rank_product_by_price(products):
    products.sort(key=lambda x: x['price'], reverse=True)
    return products
#rank product by discount
def rank_product_by_discount(products):
    products.sort(key=lambda x: x['discount'])
    return products
#reverse rank product by discount
def reverse_rank_product_by_discount(products):
    products.sort(key=lambda x: x['discount'], reverse=True)
    return products

def list_product_by_category(category):
    products = mongoDB.get_db().get_collection(collection_name).find({'category': category})
    return products

    


