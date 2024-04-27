#!/usr/bin/python3
"""Stylemate app; Application Programming Interface"""

from flask import Flask
from flask import jsonify
import json
from utils.database import Database
from utils.select_outfit import select_outfit

app = Flask(__name__)
database = Database('anomalie', 'Olaniyielect23%')

@app.route('api/v1/wardrobe', strict_slashes=False)
def get_wardrobe():
    wardrobe = {
        'tops': [],
        'bottoms': []
    }
    wardrobe['tops'] = database.get_all_cty("tops")
    wardrobe['bottoms'] = database.get_all_cty("bottoms")
    return (jsonify(wardrobe))

@app.route('api/v1/<string:cty_name>', strict_slashes=False)
def get_cty_info(cty_name):
    return (jsonify(database.get_cty(cty_name)))

@app.route('api/v1/delete/<string:table_name>/<string:cty_name>', strict_slashes=False)
def delete_cty(table_name, cty_name):
    database.delete_cty(table_name, cty_name)
    return(jsonify({}))

@app.route('api/v1/outfit/<str:theme>', strict_slashes=False)
def get_outfit(theme):
    return (jsonify(select_outfit(theme)))

@app.route('api/v1/add_info/<str:table_name>/<str:cty_name>', strict_slashes=False)
def edit_info(table_name, cty_name):
    return (jsonify(database.add_cty(cty_name, table_name)))

@app.route('api/vi/no_of_items', strict_slashes=False)
def get_no_of_items():
    return(jsonify(database.no_of_items()))

@app.route('api/v1/outfit_items', strict_slashes=False)
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