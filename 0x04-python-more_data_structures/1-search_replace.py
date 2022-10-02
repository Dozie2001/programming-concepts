#!/usr/bi/python3
def search_replace(my_list, search, replace):
    new_list =[]
    if my_list == None:
        return None
    
    for x in range(len(my_list)):
        if my_list[x] == search:
            my_list.remove(my_list[x])
            my_list.insert(x, replace)
        new_list.append(my_list[x])
    return new_list
    