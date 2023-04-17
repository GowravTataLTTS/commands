#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:29:06 2023

@author: gowrav
"""

from sqlalchemy import Column, Date, ForeignKey,Interger, Metadata,String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry
from sqlalchemy.sql import func
 

metadata = Metadata()

Base =  declarative_base(metadata=Metadata)

class Customers(Base):
    __tablename__='customers'
    name = Column(String, nullable=False)
    age = Column(String, nullable=False )
    country = Column(String, nullable=False )
    
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        
        
    def __repr__(self):
        return f"{self.name},{self.age},{self.country}"