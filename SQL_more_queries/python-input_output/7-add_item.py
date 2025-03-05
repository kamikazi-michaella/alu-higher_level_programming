#!/usr/bin/python3
"""Script that adds arguments to a Python list and saves them to a file"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except FileNotFoundError:
    json_list = []

# Append only the arguments, excluding the script name
for i in argv[1:]:
    json_list.append(i)

# Save the updated list to the file
save_to_json_file(json_list, filename)
