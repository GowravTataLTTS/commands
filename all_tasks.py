#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 19:45:04 2023

@author: gowrav
"""

from pgsql_connector import SQL
import time
from  database_connections import Customers
from prefect import task, flow
from subprocess import PIPE, Popen
import schedule
from multiprocessing import Process
from datetime import datetime
sql = SQL()

#@task
def keepalived_status():  
    state = 'FAULT STATE'
    terminal  =  Popen(['systemctl','status','keepalived.service'], 
                                  stdout=PIPE,
                                  stderr=PIPE)
    stdout,stderr=terminal.communicate()
    if stdout.decode().lower().split()[-2]=='master':
        state='MASTER STATE'
    return state

#@task
def retrive_data():
    with sql.transaction() as session:
        return session.execute('SELECT * FROM CUSTOMERS').all()

#@task
def transformation_one(data):
    country_map = {"USA":"United States","IND":"India",
                   "UK":"United Kingdom",
                   "AUS":"Australia"}
    for i in data:
        i['country'] = country_map[i['country']]
        i['name'] = '1'+ ' '+ i['name'].lower()
    time.sleep(5)
    print('first transformation is done')
    print(data)
    return data

#@task
def transformation_two(data):
    for i in data:
        i['age']= str(i['age'])+''+'Middle Age' if  i['age']>40 else str(i['age'])+' '+'Young Age'
        i['name'] =i['name'].replace('1','2')
    time.sleep(5)
    print('second transformation is done')
    print(data)
    return data

#@task
def transformation_three(data):
    country_map = {"United States":"American","India":"Indian",
                   "United Kingdom":"English",
                   "Australia":"Aussie"}
    for i in data:
        i['country'] = country_map[i['country']]
        i['name'] =i['name'].replace('2','3')
    time.sleep(5)
    print('third transformation is done')
    print(data)
    return data

#@task
def insert_data(data):
    with sql.transaction() as session:
        session.bulk_update_mappings(Customers, data)