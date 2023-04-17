#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:17:39 2023

@author: gowrav
"""
import time
from subprocess import PIPE, Popen
from prefect import flow
import schedule
from multiprocessing import Process
from datetime import datetime

"""
vrrp_instance VI_1 {
      state MASTER
      interface enp0s3
      virtual_router_id 51
      priority 244
      advert_int 1
      authentication {
         auth_type PASS
         auth_pass 12345
      }
      virtual_ipaddress {
         10.0.2.10
      }
}
"""

def keepalived_status():  
    state = 'FAULT STATE'
    terminal  =  Popen(['systemctl','status','keepalived.service'], 
                                  stdout=PIPE,
                                  stderr=PIPE)
    stdout,stderr=terminal.communicate()
    if stdout.decode().lower().split()[-2]=='master':
        state='MASTER STATE'
    return state

@flow
def trigger():    
    print('hello world')
    time.sleep(1)
    return


def prefect_checker(): 
    status = keepalived_status()
    if status == "MASTER STATE":
        trigger()
    else:
        print(datetime.now().strftime("%H:%M:%S"), "BACKUP")
    

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
