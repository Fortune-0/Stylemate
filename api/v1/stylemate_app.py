#!/usr/bin/python3
"""Stylemate app; Application Programming Interface"""

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from utils.database import Database
from utils.select_outfit import select_outfit

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
database = Database('stylemate', 'password')

@app.route('/api/v1/wardrobe', strict_slashes=False)
def get_wardrobe():
    wardrobe = {
        'tops': [],
        'bottoms': []
    }
    wardrobe['tops'] = database.get_cty_numbers("tops")
    wardrobe['bottoms'] = database.get_cty_numbers("bottoms")
    return (jsonify(wardrobe))

@app.route('/api/v1/get_info/<string:cty_name>', strict_slashes=False)
def get_cty_info(cty_name):
    cty_name = cty_name.replace("_", " ")
    return (jsonify(database.get_cty(cty_name)))

@app.route('/api/v1/delete/<string:table_name>/<string:cty_name>',
strict_slashes=False, methods=['DELETE'])
def delete_cty(table_name, cty_name):
    cty_name = cty_name.replace("_", " ")
    result = database.delete_cty(table_name, cty_name)
    return (result)

@app.route('/api/v1/outfit/<string:theme>', strict_slashes=False)
def get_outfit(theme):
    return (jsonify(select_outfit(theme.lower())))
    print(theme)

@app.route('/api/v1/add_info/<string:table_name>',
strict_slashes=False, methods=['POST'])
def edit_info(table_name):
    try:
        cty = request.get_json()
    except Exception as e:
        return (e)
    else:
        if 'name' and 'number' in cty.keys():
            return (jsonify(database.add_cty(cty, table_name)))
        else:
            return ("Invalid information supplied.\n Format: {'name':'...', 'number': '...'}")

@app.route('/api/v1/no_of_items', strict_slashes=False)
def get_no_of_items():
    return(jsonify(database.no_of_items()))

@app.route('/api/v1/outfit_items', strict_slashes=False)
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

@app.route('/api/v1/get_description', strict_slashes=False, methods=['POST'])
def handle_description():
    try:
        form_obj = request.form
    except Exception as e:
        return (e)
    else:
        #with open('random.json', 'w') as randm:
        #    rand_dict = {}
        #    for k, v in form_obj.items():
        #        rand_dict.update({k:v})
        #    json.dump(rand_dict, randm)
        #forbidden_vals = {"bottoms", "tops"}
        table_name = form_obj.get('table')
        for name, val in form_obj.items():
            if (name != 'table'):
            	cty = {'name': name, 'number': val}
            	return_val = database.add_cty(cty, table_name)
        return (jsonify("Your input has been recorded!"))
@app.route('/api/v1/set_user', strict_slashes=False, methods=['POST'])
def set_user():
    user_dict = {}
    user_obj = request.form
    if len(user_obj) != 3:
        return ("An error occurred. Please try again")
    for name, val in user_obj.items():
        user_dict.update({name: val})
    reply = database.set_user(user_dict)
    if reply == "User info updated":
        status_dict = {"new": "no"}
        with open("json_files/status.json", "w") as status:
            json.dump(status_dict, status, indent=3)
    return (reply)
@app.route('/api/v1/get_display_items', strict_slashes=False)
def get_outfit_items_for_display():
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
    return_dict = {'tops': [], 'bottoms': []}

    all_items_db.update(database.get_cty_numbers("tops"))
    all_items_db.update(database.get_cty_numbers("bottoms"))

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
    return (jsonify(return_dict))




if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
