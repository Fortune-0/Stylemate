#!/usr/bin/python3
"""Selects outfit when theme is 'formal'"""
from utils.database import Database
import json
import random

def select_formal_outfit():
    """Selects outfit from list of formal outfit combos"""
    _database = Database('anomalie', 'Olaniyielect23%')

    with open("json_files/formal_outfits.json", "r") as formal_outfits:
        outfit_data = json.load(formal_outfits)
        user_tops = _database.get_all_cty("tops")
        user_bottoms = _database.get_all_cty("bottoms")
        data_filtered = []
        gender = _database.get_user_sex()
        
        parsed_outfits = set()
        while True:
            rand_choose = random.choice(outfit_data[gender])
            parsed_outfits.add(tuple(rand_choose))
            if all(i in user_tops or i in user_bottoms for i in rand_choose):
                return (rand_choose)
            elif len(parsed_outfits) == len(outfit_data[gender]):
                return ("User does not possess enough clothing to form outfit")
            else:
                continue
    
        for key in outfit_data.keys():
            if key == theme:
                gender = top_table.get_user_sex()
                user_bottoms = top_table.get_all_cty("bottoms")
                data_unfiltered = outfit_data[key][gender]
                data_filtered = [i for i in data_unfiltered if i in user_bottoms]
                
            
                selected_bottoms = []
                selected_bottoms.append(random.choice(data_filtered))
                return (selected_bottoms)
        else:
            return ("Invalid Theme")