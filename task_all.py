"""
Created on Mon Apr 17 19:45:04 2023

@author: gowrav
"""

import time
from models import Customers, Subs, Exchange, Conflict
from prefect import task, flow
from subprocess import PIPE, Popen
import schedule
from multiprocessing import Process
from datetime import datetime
from sqlalchemy import update
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, select

metadata = MetaData()


# @task
def keepalived_status():
    terminal = Popen(['systemctl', 'status', 'keepalived.service'],
                     stdout=PIPE,
                     stderr=PIPE)
    stdout, stderr = terminal.communicate()
    return stdout.decode().upper().split()[-2]


def transaction():
    hostname = os.getenv('hostname')
    database_name = "poc_db"
    user = "postgres"
    password = "password"
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{hostname}:7432/{database_name}')
    sessionfactory = sessionmaker(bind=engine)
    session = sessionfactory()
    return session


# @task
def retrieve_completed_tasks():
    print(datetime.now().strftime("%H:%M:%S"), 'Started Retrieving Completed Tasks')
    with transaction() as session:
        subs_phone_id = session.query(Subs.phone).distinct()
        return (
            session.query(Customers.name, Customers.country, Customers.phone, Customers.email)
                .filter(~Customers.phone.in_(subs_phone_id))
                .distinct()
                .all()
        )


# @task
def transformation(data):
    print(datetime.now().strftime("%H:%M:%S"), 'Started Transformation')
    records = []
    citizen = {'USA': 'american', 'Canada': 'canadian', 'Germany': 'german',
               'Mexico': 'mexican', 'Russia': 'russian', 'France': 'french',
               'Japan': 'japanese', 'China': 'chinese', 'Brazil': 'brazilian'}
    for i in data:
        name = i.name.lower()
        email = i.email.upper()
        country = citizen[i.country] if i.country in citizen else i.country
        record = {'name': name, 'country': country, 'phone': i.phone, 'email': email}
        records.append(record)
    print(datetime.now().strftime("%H:%M:%S"), 'Completed Transformation')
    return records


# @task
def insert_data(data):
    with transaction() as session:
        print(datetime.now().strftime("%H:%M:%S"), 'Started Inserting Data')
        for i in range(9):
            session.bulk_insert_mappings(Subs, data)
            print('Inserted ', i)
        session.commit()
        print(datetime.now().strftime("%H:%M:%S"), 'Ended Inserting Data')
    return


# @task
def retrieve_exchanges():
    with transaction() as session:
        return (
            session.query(Exchange.name,Exchange.country, Exchange.phone, Exchange.email)
                .all()
        )


# @task
def database_update(data):
    with transaction as session:
        session.bulk_update_mappings(Exchange, data)
        print(datetime.now().strftime("%H:%M:%S"), 'Started Updating Database')
        session.commit()
        print(datetime.now().strftime("%H:%M:%S"), 'Completed Updating Database')
    return


# @task
def retrieve_upcoming_orders():
    with transaction() as session:
        return (
            session.query(Conflict.name, Conflict.country, Conflict.phone, Conflict.email)
                .all()
        )


# @task
def insert_conflict_ticket_data(data):
    with transaction() as session:
        session.bulk_insert_mappings(Subs, data)
        print(datetime.now().strftime("%H:%M:%S"), 'Started inserting Data in Conflict Tickets Table')
        session.commit()
        print(datetime.now().strftime("%H:%M:%S"), 'Completed inserting Data in Conflict Tickets Table')
    return
