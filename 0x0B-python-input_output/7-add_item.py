#!/usr/bin/python3

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name =add_item.json

with open(file_name, encoding="utf-8") as open_file:
    for i in range(0, sys.argv[1]):
        write_file = open_file.write(i)

     return write_file
