#!/usr/bin/python3
"""Function initialises selection process."""

from utils.select_formal_outfit import select_formal_outfit
from utils.select_top import select_top
from utils.select_bottom import select_bottom
import random

def select_outfit(mode=None, theme):
    """Calls select_top, select_bottom and other necessary functions"""

    if theme == 'formal':
        outfit = select_formal_outfit()
        return (", ".join(outfit))
    else:
        comp = random.choice([1, 2])
        outfit_top = select_top(input_dict["theme"], comp)
        outfit_bottom = select_bottom(input_dict["theme"])
    
        top_str = ""
        if comp == 2:
            top_str = "A {} and a {}".format(outfit_top[0], outfit_top[1])
        else:
            top_str = "A {}".format(outfit_top[0])
        
        bottom_str = "a {}".format(outfit_bottom[0])
    
        return ("{}, and {}".format(top_str, bottom_str))