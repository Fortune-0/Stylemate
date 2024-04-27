#!/usr/bin/python3
"""Test Database"""
from utils.database import Database
import sys

mydatabase = Database('anomalie', 'Olaniyielect23%')
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
print(sys.path)
