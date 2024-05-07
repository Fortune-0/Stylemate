#!/usr/bin/python3
"""Get all outfit clothing items in json files for display in frontend"""
import json
from utils.database import Database

database = Database("stylemate", "password")

user_sex = database.get_user_sex()
items_top_set = set()
items_bottom_set = set()

with open ("json_files/tops.json") as json_top:
    top_dict = json.load(json_top)
    for theme, item_dict in top_dict.items():
        items_list = item_dict[user_sex]
        for item in items_list:
            if type(item) == list:
                for i in item:
                    items_top_set.add(i)
            else:
                items_top_set.add(item)
with open ("json_files/bottoms.json") as json_bottom:
    bottom_dict = json.load(json_bottom)
    for theme, item_dict in bottom_dict.items():
        items_list = item_dict[user_sex]
        for item in items_list:
            items_bottom_set.add(item)
with open ("json_files/formal_outfits.json") as json_formal:
    formal_dict = json.load(json_formal)
    forms_list = formal_dict[user_sex]
    for form_fit in forms_list:
        for item in form_fit[0]:
            items_bottom_set.add(item)
        for item in form_fit[1]:
            items_top_set.add(item)
all_items = {'tops': items_top_set, 'bottoms': items_bottom_set}
all_items_db = {}
all_items_db.update(database.get_cty_numbers("tops"))
all_items_db.update(database.get_cty_numbers("bottoms"))
return_dict = {'tops': [], 'bottoms': []}
for item in all_items['tops']:
    if item in all_items_db.keys():
        return_dict['tops'].append({item: all_items_db[item]})
    else:
        return_dict['tops'].append({item: 0})
for item in all_items['bottoms']:
    if item in all_items_db.keys():
        return_dict['bottoms'].append({item: all_items_db[item]})
    else:
        return_dict['bottoms'].append({item: 0})
print(return_dict)
