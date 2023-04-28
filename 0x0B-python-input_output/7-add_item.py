#!/usr/bin/python3
"""7-add_item module to commandline args to a list to save to a json file"""

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


ac = len(argv)  # cmdline args count

try:
    my_list = list(load_from_json_file("add_item.json"))
except FileNotFoundError:
    my_list = []

if ac < 2:
    save_to_json_file(my_list, "add_item.json")

else:
    [my_list.append(argv[i]) for i in range(1, ac)]
    save_to_json_file(my_list, "add_item.json")
