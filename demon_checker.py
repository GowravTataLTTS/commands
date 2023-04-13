#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:17:39 2023

@author: gowrav
"""
import os
import subprocess
from subprocess import PIPE, Popen

os.chdir('/home/gowrav')



def something():  
    state = 'FAULT STATE'
    terminal  =  Popen(['systemctl','status','keepalived.service'], 
                                  stdout=PIPE,
                                  stderr=PIPE)
    stdout,stderr=terminal.communicate()
    decoded_stdout = stdout.decode()
    decoded_stderr = stderr.decode()
    if 'MASTER STATE' in decoded_stdout:
        terminal='MASTER STATE'
    return terminal

print(something())
