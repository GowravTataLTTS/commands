#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 19:45:04 2023

@author: gowrav
"""

#from database_connections import SQL
import time
from database_connections import Customers
from prefect import task, flow
from subprocess import PIPE, Popen
import schedule
from multiprocessing import Process
from datetime import datetime

#sql = SQL()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, select

metadata = MetaData()
columns = {"name": 0, "age": 1, "country": 2}


# @task
def keepalived_status():
    state = 'FAULT STATE'
    terminal = Popen(['systemctl', 'status', 'keepalived.service'],
                     stdout=PIPE,
                     stderr=PIPE)
    stdout, stderr = terminal.communicate()
    if stdout.decode().lower().split()[-2] == 'master':
        state = 'MASTER STATE'
    return state


def transaction():
    hostname = "localhost"
    database_name = "customers"
    user = "postgres"
    password = "nopassword"
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{hostname}:5432/{database_name}')
    sessionfactory = sessionmaker(bind=engine)
    session = sessionfactory()
    return session


# @task
def retrive_data():
    with transaction() as session:
        return session.execute(select(Customers)).scalars().all()


# @task
def transformation_one(data):
    country_map = {"USA": "United States", "IND": "India",
                   "UK": "United Kingdom",
                   "AUS": "Australia", "US": "United States"}
    new_data = []
    for i in data:
        print(i.age)
        if i.country in country_map.keys():
            i.country = country_map[i.country]
            i.name = '1' + ' ' + i.name.lower()
        all = (i.name, i.age, i.country)
        new_data.append(all)
    print('first transformation is done')
    print(new_data)
    return new_data


# @task
def transformation_two(data):
    new_data = []
    for i in data:
        if isinstance(i.age, int):
            i.age = str(i.age) + '' + 'Middle Age' if i.age > 40 else str(i.age) + ' ' + 'Young Age'
            i.name = i.name.replace('1', '2')
        all = (i.name, i.age, i.country)
        new_data.append(all)
    return new_data


# @task
def transformation_three(data):
    country_map = {"United States": "American", "India": "Indian",
                   "United Kingdom": "English",
                   "Australia": "Aussie"}
    new_data = []
    for i in data:
        if i.country in country_map.keys():
            i.country = country_map[i.country]
            i.name = i.name.replace('2', '3')
        all = (i.name, i.age, i.country)
        new_data.append(all)

    time.sleep(5)
    print('third transformation is done')
    print(new_data)
    return new_data


# @task
def insert_data(data):
    for row in data:
        with transaction() as session:
            session.execute(f'INSERT INTO public.customer_data (name, age, country) VALUES {row}')
            session.commit()
            print("inserted data", row)
