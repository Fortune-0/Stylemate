#!/usr/bin/python3
"""Function initialises selection process."""

from utils.select_formal_outfit import select_formal_outfit
from utils.select_top import select_top
from utils.select_bottom import select_bottom
import random

def select_outfit(theme, mode=None):
    """Calls select_top, select_bottom and other necessary functions"""

    if theme == 'formal':
        outfit = select_formal_outfit()
        outfit_list = []
        for part in outfit:
            for item in part:
                outfit_list.append(item)
        if type(outfit) == str:
            return (outfit)
        return (", ".join(outfit_list))
    else:
        comp = random.choice([1, 2])
        outfit_top = select_top(theme, comp)
        if type(outfit_top) == str:
            return (outfit_top)
        outfit_bottom = select_bottom(theme)
        if type(outfit_bottom) == str:
            return (outfit_bottom)

        top_str = ""
        if comp == 2:
            top_str = "A {} and a {}".format(outfit_top[0][0], outfit_top[0][1])
        else:
            print(outfit_top)
            top_str = "A {}".format(outfit_top[0])
        print(outfit_bottom)
        bottom_str = "a {}".format(outfit_bottom[0])

        return ("{}, and {}".format(top_str, bottom_str))
