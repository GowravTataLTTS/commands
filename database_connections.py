#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:04:04 2023

@author: gowrav
"""

from sqlalchemy import Column, MetaData, Text, Integer
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()

hostname = "localhost"
database_name = "customers"
user = "postgres"
password = "postgres"

Base = declarative_base(metadata=metadata)


class Customers(Base):
    __tablename__ = 'customer_data'
    name = Column(Text, nullable=False, primary_key=True)
    age = Column(Integer, nullable=False)
    country = Column(Text, nullable=False)

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def __repr__(self):
        return f"{self.name},{self.age},{self.country}"
