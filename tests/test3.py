#!/usr/bin/python3
"""Test select_outfit function"""

from utils.select_outfit import select_outfit
from utils.database import Database

database = Database('anomalie', 'Olaniyielect23%')
database.add_cty({"name": "suit skirt", "number": 3}, "tops")
database.add_cty({"name": "suit", "number": 3}, "tops")
database.add_cty({"name": "camisole", "number": 7}, "tops")
database.add_cty({"name": "jacket", "number": 7}, "tops")
database.add_cty({"name": "plaid skirt", "number": 7}, "tops")

outfit = select_outfit("formal")
print(outfit)

