#!/usr/bin/python3
# 3-to_json_string.py

"""Function that returns json string"""

import json


def to_json_string(my_obj):
    """returns json representation of an object"""

    return json.dumps(my_obj)
