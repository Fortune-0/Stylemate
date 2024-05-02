#!/usr/bin/python3
"""Stylemate app; Application Programming Interface"""

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from utils.database import Database
from utils.select_outfit import select_outfit

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
database = Database('stylemate', 'password')

@app.route('/api/v1/wardrobe', strict_slashes=False)
def get_wardrobe():
    wardrobe = {
        'tops': [],
        'bottoms': []
    }
    wardrobe['tops'] = database.get_cty_numbers("tops")
    wardrobe['bottoms'] = database.get_cty_numbers("bottoms")
    return (jsonify(wardrobe))

@app.route('/api/v1/get_info/<string:cty_name>', strict_slashes=False)
def get_cty_info(cty_name):
    cty_name = cty_name.replace("_", " ")
    return (jsonify(database.get_cty(cty_name)))

@app.route('/api/v1/delete/<string:table_name>/<string:cty_name>',
strict_slashes=False, methods=['DELETE'])
def delete_cty(table_name, cty_name):
    cty_name = cty_name.replace("_", " ")
    result = database.delete_cty(table_name, cty_name)
    return (result)

@app.route('/api/v1/outfit/<string:theme>', strict_slashes=False)
def get_outfit(theme):
    return (jsonify(select_outfit(theme.lower())))
    print(theme)

@app.route('/api/v1/add_info/<string:table_name>',
strict_slashes=False, methods=['POST'])
def edit_info(table_name):
    try:
        cty = request.get_json()
    except Exception as e:
        return (e)
    else:
        if 'name' and 'number' in cty.keys():
            return (jsonify(database.add_cty(cty, table_name)))
        else:
            return ("Invalid information supplied.\n Format: {'name':'...', 'number': '...'}")

@app.route('/api/v1/no_of_items', strict_slashes=False)
def get_no_of_items():
    return(jsonify(database.no_of_items()))

@app.route('/api/v1/outfit_items', strict_slashes=False)
def get_outfit_items():
    outfit_items = {
        'outfit_tops': {},
        'outfit_bottoms': {},
        'formal_outfits': {}
        }
    with open ("json_files/tops.json") as tops:
        outfit_items['outfit_tops'] = json.load(tops)
    with open ("json_files/bottoms.json") as bottoms:
        outfit_items['outfit_bottoms'] = json.load(bottoms)
    with open ("json_files/formal_outfits.json") as formal_outfits:
        outfit_items['formal_outfits'] = json.load(formal_outfits)
    return (jsonify(outfit_items))


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
