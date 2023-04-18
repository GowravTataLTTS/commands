#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:55:22 2023

@author: gowrav
"""
import random

first_name = ['Ayan', "Brad", "Chetan", "David", "Eswar"]
last_name = ["Reddy", "Smith", "Naidu", "Abbas", "Jenkovich"]

names = []
for i in range(5):
    country = ['IND', 'USA', 'UK', 'AUS']
    name = random.choice(first_name) + ' ' + random.choice(last_name)
    country = random.choice(country)
    age = random.choice(list(range(18, 61)))

    new_names = {'name': name,
                 'age': age,
                 'country': country}
    names.append(new_names)


def transformation_one(data):
    country_map = {"USA": "United States", "IND": "India",
                   "UK": "United Kingdom",
                   "AUS": "Australia"}
    for i in data:
        if i['country'] in country_map.keys():
            i['country'] = country_map[i['country']]
            i['name'] = i['name'].replace('1', '2')
    return data


def transformation_two(data):
    for i in data:
        if isinstance(i['age'], int):
            i['age'] = str(i['age']) + ' ' + 'Middle Age' if i['age'] > 40 else str(i['age']) + ' ' + 'Young Age'
            i['name'] = i['name'].replace('2', '3')
    return data


def transformation_three(data):
    country_map = {"United States": "American", "India": "Indian",
                   "United Kingdom": "English",
                   "Australia": "Aussie"}
    for i in data:
        if i['country'] in country_map.keys():
            i['country'] = country_map[i['country']]
            i['name'] = '3' + ' ' + i['name'].lower()
    return data


all_names = transformation_one(names)
second_names = transformation_two(all_names)
third_names = transformation_three(second_names)

print(third_names)
