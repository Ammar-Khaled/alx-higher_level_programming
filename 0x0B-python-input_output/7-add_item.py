#!/usr/bin/python3
""" This module adds all arguments to a Python list,
    and then save them to a file."""

import sys
import os.path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

data_list = []

if os.path.exists('add_item.json'):
    data_list = load_from_json_file('add_item.json')

for item in sys.argv[1:]:
    data_list.append(item)

save_to_json_file(data_list, 'add_item.json')
