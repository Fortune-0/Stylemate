#!/usr/bin/python3
"""Select_bottom function for selecting bottom category"""
from utils.database import Database
import json
import random

def select_bottom(theme):
    """Select bottom randomly from list of 'bottom' items based in theme"""
    _database = Database('stylemate', 'password')

    # Open json file and retrieve all clothing item categories based on theme and sex
    with open("json_files/outfit_bottoms.json", "r") as outfit_bottoms:
        outfit_data = json.load(outfit_bottoms)

        for key in outfit_data.keys():
            if key == theme:
                # Perform filtering based on sex
                gender = _database.get_user_sex()
                # Get user's wardrobe items without 0 number value
                user_bottoms = database.get_cty_numbers("bottoms")
                user_bottoms = {k: v for k, v in user_bottoms.items() if v > 0}
                data_unfiltered = outfit_data[key][gender]
                # Filter to obtain list of clothing item categories present in user's wardrobe
                data_filtered = [i for i in data_unfiltered if i in user_bottoms]
                if len(data_filtered) == 0:
                    return("User does not possess enough bottoms to form outfit")

                selected_bottoms = []
                selected_bottoms.append(random.choice(data_filtered))
                return (selected_bottoms)
        else:
            return ("Invalid Theme")
