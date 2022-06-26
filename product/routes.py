
from flask import Blueprint
from product.models import Product
from flask import Flask, jsonify, redirect, request, session

product_blueprint = Blueprint('product_blueprint', __name__)


@product_blueprint.route('/create-product',methods=['POST'])
def CreateProduct():
  return Product().create_product()

@product_blueprint.route('/update-product/<product_id>',methods=['POST'])
def UpdateProduct(product_id):
  return Product().update_product(product_id)

@product_blueprint.route('/delete-product/<product_id>', methods=['POST'])
def DeleteProduct(product_id):
    return Product().delete_product(product_id)
