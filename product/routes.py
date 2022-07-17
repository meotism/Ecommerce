
from flask import Blueprint
from flask import Flask, jsonify, redirect, request, session
from product.models import Product

product_blueprint = Blueprint('product_blueprint', __name__)


@product_blueprint.route('/create-product',methods=['POST'])
def new_func():
    return Product().createProduct()

@product_blueprint.route('/update-product/<product_id>',methods=['POST'])
def UpdateProduct(product_id):
  return Product().updateproduct(product_id)

@product_blueprint.route('/delete-product/<product_id>', methods=['POST'])
def DeleteProduct(product_id):
    return Product().deleteproduct(product_id)

@product_blueprint.route('/getproducts', methods = ['GET'])
def getAllProduct():
    return Product().getallproduct()