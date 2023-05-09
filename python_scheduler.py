#!/usr/bin/python3
"""
Created on Mon Apr 17 17:47:18 2023

@author: gowrav
"""

from prefect import task, flow
from task_all import *
import schedule
from multiprocessing import Process
from datetime import datetime


# @flow
def trigger():
    first_data = retrieve_completed_tasks()
    first_transformation = transformation(first_data)
    first_insert = insert_data(first_transformation)

#    second_data = retrieve_exchanges()
#    second_transformation = transformation(second_data)
#    second_update = database_update(second_transformation)
#
#    third_data = retrieve_upcoming_orders()
#    third_transformation = transformation(third_data)
#    third_insert = insert_conflict_ticket_data(third_transformation)

    return


def prefect_checker():
    print(datetime.now().strftime("%H:%M:%S"), 'Entered Flow')
    status = keepalived_status()
    print(datetime.now().strftime("%H:%M:%S"), f'Status of keepalived is {status}')
    if status == "MASTER":
        trigger()
        print(datetime.now().strftime("%H:%M:%S"), "Flow is completed")
    else:
        print(datetime.now().strftime("%H:%M:%S"), "BACKUP")


def run_per_time():
    print(datetime.now().strftime("%H:%M:%S"), 'Scheduler Triggered')
    schedule.every(1).minute.do(prefect_checker)
    while True:
        schedule.run_pending()


def run_job():
    print(datetime.now().strftime("%H:%M:%S"), 'Entered Run Job')
    p = Process(target=run_per_time)
    p.start()
    p.join()


if __name__ == '__main__':
    trigger()
