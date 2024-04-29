#!/usr/bin/python3
"""Test Database"""
import sys
sys.path.append('/home/anoly23/Stylemate')
print(sys.path)
from utils.database import Database
mydatabase = Database('stylemate', 'password')
add_dict = {
        'name': 'shawl',
        'number': 10
        }
add_dict1 = {
        'name': 'jean trousers',
        'number': 8
        }
mydatabase.add_cty(add_dict, "tops")
mydatabase.add_cty(add_dict1, "bottoms")
print(mydatabase.get_all_cty("tops"))
