from flask import Flask, jsonify, redirect, request, session
from config.db import MongoDB
import json
import uuid
import datetime

collection_name = "product"

mongoDB = MongoDB()

class Product:
  def __init__(self):
    self.collection = mongoDB.get_db().get_collection(collection_name)
  def createProduct(self):
    # Create the product object
    product = {
    "_id": uuid.uuid4().hex,
    "name": request.form.get('name'),
    "ammount": request.form.get('ammount'),
    "price":request.form.get('price'),
    "category":"",
    "desc": request.form.get('desc'),
    "image":"",
    "modified_date": datetime.datetime.now(),
    }
    self.collection.insert_one(product)
    return jsonify(product), 200

  def updateproduct(product_id, self):
        product = {
            "name": request.form.get('name'),
            "ammount": request.form.get('ammount'),
            "price":request.form.get('price'),
            "category":"",
            "desc": request.form.get('desc'),
            "image":"",
            "modified_date": datetime.datetime.now(),
        }
        if self.collection.update_one({'_id': product_id}, {'$set': product}):
            return jsonify(product), 200

  def deleteproduct(product_id,self):
        if self.collection.delete_one({'_id': product_id}):
            return jsonify({}), 200

  def getproductbycategory(category,self):
        products = self.collection.find({'category': category})
        return products
  def getproductbyname(name,self):
        products = self.collection.find({'name': name})
        return products

    #rank product by price
  def rankproductbyprice(self):
        self.sort(key=lambda x: x['price'])
        return self
    #reverse rank product by price
  def reverserankproductbyprice(self):
        self.sort(key=lambda x: x['price'], reverse=True)
        return self
  def listproductbycategory(category, self):
        products = self.collection.find({'category': category})
        return products
  def getallproduct(self):
        products = self.collection.find()
        return products



