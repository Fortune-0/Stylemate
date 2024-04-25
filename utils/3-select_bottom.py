#!/usr/bin/python3
"""Select_bottom function for selecting bottom category"""
from database import Database
import json
import random

def select_bottom(theme, comps):
    """Selects bottom randomly from list of 'bottom' items"""
    _database = Database()

    with open("outfit_items/outfit_bottoms.json", "r") as outfit_botttoms:
        outfit_data = json.load(outfit_bottoms)
        data_filtered = []
    
        for key in outfit_data.keys():
            if key == theme:
                gender = _database.get_user_sex()
                user_bottoms = _database.get_all_cty("bottoms")
                data_unfiltered = outfit_data[key][gender]
                data_filtered = [i for i in data_unfiltered if i in user_bottoms]
                
            
                selected_bottoms = []
                selected_bottoms.append(random.choice(data_filtered))
                return (selected_bottoms)
        else:
            return ("Invalid Theme")