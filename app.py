import re
import os
import math
import uuid
from flask import Flask, request, jsonify
from logging import FileHandler, WARNING


def create_app():
    flask_app = Flask(__name__)
    flask_app.debug = True # give out errors in cmd for flask 
    port = int(os.environ.get('PORT', 5000))
    flask_app.run(debug=True,  port=port)
    return flask_app


uuid_dict = {} # in-memory storage, else we can use sqlite for temporary database to survive application restarts
               # for permanent database, Redis can be used
app = create_app()

file_handler = FileHandler('errorlog.txt') # Error log 
file_handler.setLevel(WARNING)


def handle_bad_request(e):
    return 'bad request!', 400


app.register_error_handler(400, handle_bad_request)


@app.route("/")
def bad_error_handling_lol():
    return "Why are you here? You might have done something wrong. But the initial setup works."


@app.route('/receipts/<id>/points', methods=['GET'])
def get_points(id):  ### If you want the id to survive application restart, sqlite can be used
    if id in uuid_dict:
        points = uuid_dict[id]
        response = {"points" : points}
    else:
        response = {"Error":"Invalid Receipt"}
    
    return jsonify(response)


@app.route("/receipts/process", methods=["POST"])
def generate_receipt_id():
    receipt_data = request.get_json()
    
    id = str(uuid.uuid4())
    # print(id)
    points_awarded = calculate_points(receipt_data)
    uuid_dict[id] = points_awarded

    return {"id" : id}


def calculate_points(receipt_data):
    points = 0
    # Rule 1, alphanumeric character
    points += len([char for char in receipt_data['retailer'] if char.isalnum()])

    # Rule 2, 50 points for no cents
    if float(receipt_data['total']) == round(float(receipt_data['total'])): # here Error handling can be intrdouced to handle invalid type
        points += 50

    # Rule 3 25 cents
    if float(receipt_data['total']) % 0.25 == 0:
        points += 25

    # Rule 4 two items
    even_items = len(receipt_data['items']) // 2
    points += even_items * 5

    #Rule 5 Trimeed Length
    for item in receipt_data['items']:
        if len(item['shortDescription'].strip()) % 3 == 0:
            price = float(item['price'])
            points += math.ceil(price * 0.2)
    
    #Rule 6 date of purchase
    if int(receipt_data['purchaseDate'].split('-')[2]) % 2 == 1:
        points += 6
    
    #Rule 7
    if "16:00" > receipt_data['purchaseTime'] > "14:00":
        points += 10
    
    return points

