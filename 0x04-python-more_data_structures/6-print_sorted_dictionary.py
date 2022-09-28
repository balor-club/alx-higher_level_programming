#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_dictionary = OrderedDict(sorted(dict.items()))
    print(new_dictionary)
