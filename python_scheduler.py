#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:47:18 2023

@author: gowrav
"""

from prefect import task, flow
from all_tasks import keepalived_status, retrieve_completed_tasks, transformation_one, insert_data
import schedule
from multiprocessing import Process
from datetime import datetime


#@flow
def trigger():
    names = retrieve_completed_tasks()
    all_names = transformation_one(names)
    insert_data(all_names)
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
