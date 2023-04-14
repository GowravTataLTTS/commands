#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:17:39 2023

@author: gowrav
"""
import time
import subprocess
from subprocess import PIPE, Popen
from prefect import task, flow
import subprocess
import schedule
from multiprocessing import Process

def keepalived_status():  
    state = 'FAULT STATE'
    terminal  =  Popen(['systemctl','status','keepalived.service'], 
                                  stdout=PIPE,
                                  stderr=PIPE)
    stdout,stderr=terminal.communicate()
    decoded_stdout = stdout.decode()
    decoded_stderr = stderr.decode()
    if stdout.decode().lower().split()[-2]=='master':
        state='MASTER STATE'
    return state

@flow
def trigger():    
    print('hello world')
    time.sleep(1)


def prefect_checker(): 
    status = keepalived_status()
    if status == "MASTER STATE":
        trigger()
    

def run_per_time():
    schedule.every(10).seconds.do(prefect_checker)
    while True:
        schedule.run_pending()




def run_job():
    p=Process(target=run_per_time)
    p.start()
    p.join()
    
    
if __name__=='__main__':
    run_job()
