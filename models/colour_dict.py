#!/usr/bin/python3
"""Dictionary that stores common colours"""
from models.base import BaseItem

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
    "teal": "0,128,128"
})


col = input(" what colour do u want? ")
print(f"The RGB value for you desired colour is: ({colours_dict[col]})")