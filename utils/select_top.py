#!/usr/bin/python3
"""Select_top function for selecting top category"""
from utils.database import Database
import json
import random

def select_top(theme, comp):
    """Selects top randomly from list of 'top' items"""
    database = Database('anomalie', 'Olaniyielect23%')

    with open("json_files/tops.json", "r") as outfit_tops:
        outfit_data = json.load(outfit_tops)
        data_filtered = []
    
        for key in outfit_data.keys():
            if key == theme:
                gender = database.get_user_sex()
                user_tops = database.get_all_cty("tops")
                data_unfiltered = outfit_data[key][gender]
                data_filtered = []
                for item in data_unfiltered:
                    if type(item) == str and item in user_tops:
                        data_filtered.append(item)
                    elif type(item) == list and all(i in user_tops for i in item):
                        data_filtered.append(item)
                    else:
                        continue 
                if len(data_filtered) == 0:
                    return ([])
            
                selected_tops = []
                if comp == 1:
                    selected_tops.append(random.choice([i for i in data_filtered if type(i) != list]))
                if comp == 2:
                    selected_tops.append(random.choice([i for i in data_filtered if type(i) == list]))
                return (selected_tops)
        if theme not in outfit_data.keys():
            return ("Invalid Theme")
