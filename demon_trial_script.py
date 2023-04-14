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


@task
def check_status():  
    state = 'BACKUP'
    terminal  =  Popen(['systemctl','status','keepalived.service'], 
                                  stdout=PIPE,
                                  stderr=PIPE)
    stdout,stderr=terminal.communicate()
    decoded_stdout = stdout.decode().lower()
    master = ['master state' in decoded_stdout,
              'fault state' not in decoded_stdout,
              'higher priority' not in decoded_stdout]
    if stdout.decode().lower().split()[-2]=='master':
    #if all(master):
        state='MASTER'
    return state


@flow
def trigger():
    status = check_status()
    if status == "MASTER":
        print('hello world')
        time.sleep(10)
        return 
    print('fault block')
    return 


if __name__=='__main__':
	trigger()            


