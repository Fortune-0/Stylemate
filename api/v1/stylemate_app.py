#!/usr/bin/python3
"""Stylemate app; Application Programming Interface"""
from flask import Flask
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
    return (wardrobe)

@app.route('api/v1/<string:cty_name>', strict_slashes=False)
def get_cty_info(cty_name):
    return (database.get_cty(cty_name))

@app.route('api/v1/delete/<string:table_name>/<string:cty_name>', strict_slashes=False)
def delete_cty(table_name, cty_name):
    database.delete_cty(table_name, cty_name)

@app.route('api/v1/outfit/<str:theme>')
def get_outfit(theme):
    return (select_outfit(theme))


