#!/usr/bin/python3
"""Test select_outfit function"""

import sys
sys.path.append('/home/anoly23/Stylemate')
from utils.select_outfit import select_outfit
from utils.database import Database

database = Database('stylemate', 'password')
database.add_cty({"name": "suit skirt", "number": 3}, "bottoms")
database.add_cty({"name": "suit", "number": 3}, "tops")
database.add_cty({"name": "camisole", "number": 7}, "tops")
database.add_cty({"name": "jacket", "number": 7}, "tops")
database.add_cty({"name": "", "number": 7}, "tops")
database.add_cty({"name": "plaid skirt", "number": 7}, "bottoms")

outfit = select_outfit("formal")
print(outfit)

