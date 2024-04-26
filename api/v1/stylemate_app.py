#!/usr/bin/python3
"""Stylemate app; Application Programming Interface"""
from flask import Flask
from utils.database import Database

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

@app.route('api/v1/<string:cty_name', strict_slashes=False)
def get_cty_info(cty_name):
    
