#!/usr/bin/python3
"""
Created on Mon Apr 17 17:47:18 2023

@author: gowrav
"""
from prefect import task, flow
from only_for_prefect import *
import schedule
from multiprocessing import Process
from datetime import datetime


@flow
def trigger():
    status = keepalived_status()
    if status=='MASTER':
        first_data = retrieve_completed_tasks()
        first_transformation = transformation(first_data)
        first_insert = insert_data(first_transformation)

        second_data = retrieve_exchanges()
        second_transformation = transformation(second_data)
        second_update = database_update(second_transformation)

        third_data = retrieve_upcoming_orders()
        third_transformation = transformation(third_data)
        third_insert = insert_conflict_ticket_data(third_transformation)    
        return

