#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:16:46 2019

@author: abhijithneilabraham
"""

import io

def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
#    data = {}
#    for line in fin:
#        tokens = line.rstrip().split(' ')
#        data[tokens[0]] = map(float, tokens[1:])
#    return data
    print(d)
embed=load_vectors('/Users/abhijithneilabraham/Downloads/useful_stuff/mal')
