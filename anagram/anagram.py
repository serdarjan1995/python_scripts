#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python script for comparing two strings whether they are anagrams or not

Created on Thu Oct 22 14:05:16 2020

@author: Sardor
@version: 1.0.0
@python_v: 3.7
"""

def main():
    str_a = input("a: ")
    str_b = input("b: ")
    if sorted(str_a) == sorted(str_b):
        print("They are anagrams")
    else:
        char_map_a = dict((c, str_a.count(c)) for c in str_a)
        char_map_b = dict((c, str_b.count(c)) for c in str_b)
        char_remove_a = 0
        char_remove_b = 0
        
        #combine all unique chars from 2 strings and iterate
        for c in set(list(char_map_a.keys()) + list(char_map_b.keys())):
            if c not in char_map_b.keys():       # char is not in str_b
                char_remove_a += char_map_a[c]   # remove all occurances
                continue                         # from str_a
            
            if c not in char_map_a.keys():       # char is not in str_a
                char_remove_b += char_map_b[c]   # remove all occurances
                continue                         # from str_b
            
            diff = char_map_a[c] - char_map_b[c] # calculate difference
            if diff > 0:                         # freq higher in str_a
                char_remove_a += diff
            elif diff < 0:                       # freq higher in str_b
                char_remove_b += abs(diff)
        
        print("Remove %d characters from '%s' and %d characters from '%s'"
              % (char_remove_a, str_a, char_remove_b, str_b) )
            

if __name__ == "__main__":
    main()
