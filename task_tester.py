#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:55:22 2023

@author: gowrav
"""



names = [{'name': 'Isaiah Morgan', 'age': 27, 'country': 'USA'}, {'name': 'Anand Morgan', 'age': 54, 'country': 'IND'}, {'name': 'Anand Naidu', 'age': 25, 'country': 'AUS'}, {'name': 'James Anderson', 'age': 19, 'country': 'AUS'}, {'name': 'Andrew Naidu', 'age': 35, 'country': 'AUS'}]

def transformation_one(data):
    country_map = {"USA":"United States","IND":"India",
                   "UK":"United Kingdom",
                   "AUS":"Australia"}
    for i in data:
        i['country'] = country_map[i['country']]
        i['name'] =i['name'].replace('1','2')
    return data

def transformation_two(data):
    for i in data:
        i['age']= str(i['age'])+''+'Middle Age' if  i['age']>40 else str(i['age'])+' '+'Young Age'
        i['name'] =i['name'].replace('2','3')
    return data

def transformation_three(data):
    country_map = {"United States":"American","India":"Indian",
                   "United Kingdom":"English",
                   "Australia":"Aussie"}
    for i in data:
        i['country'] = country_map[i['country']]
        i['name'] = '3'+ ' '+ i['name'].lower()
    return data




all_names = transformation_one(names)
second_names = transformation_two(all_names)
third_names = transformation_three(second_names)

print(third_names)