#!/usr/bin/python3
"""Selects outfit when theme is 'formal'"""
from utils.database import Database
import json
import random

def select_formal_outfit():
    """Selects outfit from list of formal outfit combos"""
    _database = Database('stylemate', 'password')

    with open("json_files/formal_outfits.json", "r") as formal_outfits:
        outfit_data = json.load(formal_outfits)
        user_bottoms = database.get_cty_numbers("bottoms")
        user_bottoms = {k: v for k, v in user_bottoms.items() if v > 0}
        user_tops = database.get_cty_numbers("tops")
        user_tops = {k: v for k, v in user_tops.items() if v > 0}

        data_filtered = []
        gender = _database.get_user_sex()

        parsed_outfits = set()
        while True:
            rand_choose = random.choice(outfit_data[gender])
            # Access top and bottom parts of each formal outfit using list index
            tup_top = tuple(i if type(i) != list else i for i in rand_choose[0])
            tup_bottom = tuple(i if type(i) != list else i for i in rand_choose[1])
            rand_choose_tup = (tup_top, tup_bottom)

            parsed_outfits.add(tuple(rand_choose_tup))
            # List of all clothing items in chosen outfit
            all_items = []
            for part in rand_choose:
                for item in part:
                    all_items.append(item)
            if all(i in user_tops or i in user_bottoms for i in all_items):
                return (rand_choose)
            # Return if user does not have any of the clothing items in the 
            # application's featured clothing items
            elif len(parsed_outfits) == len(outfit_data[gender]):
                return ("User does not possess enough clothing to form outfit")
            else:
                continue
