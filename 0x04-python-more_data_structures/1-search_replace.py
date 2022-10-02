#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    if my_list is None:
        return None
    else:
        new_list = my_list[:]

    for x in range(len(new_list)):
        if new_list[x] == search:
            new_list.remove(new_list[x])
            new_list.insert(x, replace)
    return new_list
