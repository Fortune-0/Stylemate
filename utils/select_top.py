#!/usr/bin/python3
"""Select_top function for selecting top category"""
from utils.database import Database
import json
import random

def select_top(theme, no_tops):
    """Selects top randomly from list of 'top' items"""
    database = Database('stylemate', 'password')

    with open("json_files/outfit_tops.json", "r") as outfit_tops:
        outfit_data = json.load(outfit_tops)
        data_filtered = []

        for key in outfit_data.keys():
            if key == theme:
                # Perform filtering based on sex
                gender = database.get_user_sex()
                # Get user's wardrobe items without 0 number value
                user_tops = database.get_cty_numbers("tops")
                user_tops = {k: v for k, v in user_tops.items() if v > 0}
                print(user_tops)
                data_unfiltered = outfit_data[key][gender]
                # Filter to obtain list of clothing item categories present in user's wardrobe
                data_filtered = []
                for item in data_unfiltered:
                    # Handle string-type top category 
                    if type(item) == str and item in user_tops:
                        data_filtered.append(item)
                    # Handle list-type top category
                    elif type(item) == list and all(i in user_tops for i in item):
                        data_filtered.append(item)
                    else:
                        continue
                if len(data_filtered) == 0:
                    return ("User does not possess enough clothes to form outfit.")

                selected_tops = []
                # Do not select top category with list
                if no_tops == 1:
                    selected_tops.append(random.choice([i for i in data_filtered if type(i) != list]))
                # Select top category with list
                if no_tops == 2:
                    list_of_lists = [i for i in data_filtered if type(i) == list]
                    if len(list_of_lists) == 0:
                        selected_tops.append(random.choice(data_filtered))
                    else:
                        selected_tops.append(random.choice(list_of_lists))
                return (selected_tops)
        if theme not in outfit_data.keys():
            return ("Invalid Theme")
