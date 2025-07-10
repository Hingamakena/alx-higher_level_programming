#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for i in my_list:
        if search in my_list:
            my_list[search] = replace
