#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:47:18 2023

@author: gowrav
"""
#from database_connections import SQL
from prefect import task, flow
from all_tasks import keepalived_status, retrive_data, transformation_one, transformation_two, transformation_three, \
    insert_data
import schedule
from multiprocessing import Process
from datetime import datetime

#sql = SQL()


# @flow
def trigger():
    names = retrive_data()
    all_names = transformation_one(names)
    # second_names = transformation_two(all_names)
    # third_names = transformation_three(second_names)
    insert_data(all_names)
    return


def prefect_checker():
    status = keepalived_status()
    if status == "MASTER STATE":
        trigger()
    else:
        print(datetime.now().strftime("%H:%M:%S"), "BACKUP")


def run_per_time():
    schedule.every(1).minute.do(prefect_checker)
    while True:
        schedule.run_pending()


def run_job():
    p = Process(target=run_per_time)
    p.start()
    p.join()


if __name__ == '__main__':
    prefect_checker()
