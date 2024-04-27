#!/usr/bin/python3
"""Test select_top function"""
from utils.select_top import select_top
from utils.select_bottom import select_bottom

outfit_top = select_top('casual', 2)
outfit_bottom = select_bottom('casual')
print(outfit_top)
print(outfit_bottom)
