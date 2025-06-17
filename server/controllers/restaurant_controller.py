from flask import Blueprint, jsonify

bp = Blueprint("restaurants", __name__, url_prefix="/restaurants")

bp.route('/')
def index ():
    return jsonify({'message':'Here are all restaurants'})