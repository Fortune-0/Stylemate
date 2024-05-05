#!/usr/bin/python3
"""Serialise outfit items data to json files"""

import json

colours_dict = dict({
    "red" : "255,0,0" ,  # RGB Hex Code for Red
    "green": "0,128,0", # RGB Hex Code for Green
    "blue": "0,0,255",  # RGB HEX Code for Blue
    "white": "255,255,255",   # RGB Hex Code for White
    "black": "0,0,0",          # RGB Hex Code for Black
    "yellow": "255,255,0",     # Yellow Color in RGB
    "navl blue":  "0,68,174", # Navy Blue color in RGB
    "gold": "255,193,0",
    "pink": "255,192,203",
    "orange": "255,165,0",
    "cyan": "0,255,255",
    "magenta": "255,0,255",
    "brown": "165,42,42",
    "lime": "0,255,0",
    "purple": "128,0,128",
    "tan": "210,180,140",
    "teal": "0,128,128",
    "olive": "128,128,0",
    "light brown": "181,101,29",
    "bronze": "205,127,50",
    "ochre": "204,119,34",
    "black bean": "61,12,2",
    "dark salmon": "233,150,122",
    "chocolate": "210,105,30",
    "sky blue": "135,206,235",
    "royal blue": "65,105,225",
    "dark blue": "0,0,139",
    "cobalt": "0,71,171",
    "imperial blue": "0,35,149",
    "grey": "128,128,128",
    "light grey": "211,211,211",
    "violet": "143,0,255",
    "indigo": "75,0,130",
})

outfit_tops_dict = {
    'casual': {
        'male': ['t-shirt', ['round-necked sweater', 'collared shirt'], 'plain Top'],
        'female': ['plain blouse', ['sleeveless top', 'shawl'], 'turtle-necked top']
        },
    'dinner': {
        'male': ['silk button-down shirt', 'plaid T-shirt'],
        'female': ['flowered blouse', 'top with flared sleeves']
        },
    'exercise': {
        'male': ['sweatshirt', 'sleeveless top'],
        'female': ['sleeveless breathable top', 'light long-sleeved cotton blouse']
    }
}

outfit_bottoms_dict = {
    'casual': {
        'male': ['jean trousers', 'cargos', 'khaki shorts'],
        'female': ['flared skirt', 'straight skirt', 'leggings', 'jean trousers']
        },
    'dinner': {
        'male': ['pants trousers', 'silk trousers'],
        'female': ['skirt', 'flared skirt']
        },
    'exercise': {
        'male': ['shorts', '3/4 shorts'],
        'female': ['biker shorts', 'leggings']
    }
}

status_dict = {'new': 'yes'}

formal_outfits_dict = {
    'female': [['suit skirt', 'suit'], ['jacket', 'camisole', 'plaid skirt']],
    'male': [['tuxedo'], ['suit', 'shirt', 'trousers']]
}

while False:
    try:
        col = input("What color do you want? ")
        rgb_value = colours_dict.get(col.lower(), "Color not found")
        print(f"The RGB value for your desired color is: ({rgb_value})")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

with open ("json_files/colours.json", "w") as json_colour:
    json.dump(colours_dict, json_colour, indent = 3)
with open ("json_files/tops.json", "w") as json_top:
    json.dump(outfit_tops_dict, json_top, indent = 3)
with open ("json_files/bottoms.json", "w") as json_bottom:
    json.dump(outfit_bottoms_dict, json_bottom, indent = 3)
with open ("json_files/formal_outfits.json", "w") as json_formal:
    json.dump(formal_outfits_dict, json_formal, indent = 3)
with open ("json_files/status.json", "w") as json_status:
    json.dump(status_dict, json_status, indent = 3)
