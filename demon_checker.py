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

os.chdir('/home/gowrav')


@task
def check_status():  
    state = 'FAULT STATE'
    terminal  =  Popen(['systemctl','status','keepalived.service'], 
                                  stdout=PIPE,
                                  stderr=PIPE)
    stdout,stderr=terminal.communicate()
    decoded_stdout = stdout.decode()
    decoded_stderr = stderr.decode()
    if 'MASTER STATE' in decoded_stdout:
        state='MASTER STATE'
    return state


@flow
def trigger():
    status = check_status()
    if status == "MASTER STATE":
        print('entered into master state block')
        time.sleep(10)
        return 
    print('entered into fault state block')
    time.sleep(5)
    return 


            


