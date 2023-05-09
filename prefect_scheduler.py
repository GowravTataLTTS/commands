#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:47:18 2023

@author: gowrav
"""
from prefect import task, flow
from task_all import keepalived_status, retrive_data, transformation_one, transformation_two, transformation_three, \
    insert_data
import schedule
from multiprocessing import Process
from datetime import datetime


@flow
def trigger():
    names = retrive_data()
    all_names = transformation_one(names)
    second_names = transformation_two(all_names)
    third_names = transformation_three(second_names)
    insert_data(third_names)
    return
