#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:47:18 2023

@author: gowrav
"""
#from prefect import task
from pgsql_connector import SQL
import time
from  pgsql_connector import Customers
sql = SQL()



def retrive_data():
    with sql.transaction() as session:
        return session.execute('SELECT * FROM CUSTOMERS').all()


def transformation_one(data):
    country_map = {"USA":"United States","IND":"India",
                   "UK":"United Kingdom",
                   "AUS":"Australia"}
    for i in data:
        i['country'] = country_map[i['country']]
        i['name'] = '1'+ ' '+ i['name'].lower()
    time.sleep(5)
    return data

def transformation_two(data):
    for i in data:
        i['age']= str(i['age'])+''+'Middle Age' if  i['age']>40 else str(i['age'])+' '+'Young Age'
        i['name'] =i['name'].replace('1','2')
    time.sleep(5)
    return data

def transformation_three(data):
    country_map = {"United States":"American","India":"Indian",
                   "United Kingdom":"English",
                   "Australia":"Aussie"}
    for i in data:
        i['country'] = country_map[i['country']]
        i['name'] =i['name'].replace('2','3')
    time.sleep(5)
    return data



def insert_data(data):
    with sql.transaction() as session:
        session.bulk_update_mappings(Customers, data)