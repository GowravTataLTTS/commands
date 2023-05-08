#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:04:04 2023

@author: gowrav
"""

from sqlalchemy import Column, MetaData, Text, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
import os

metadata = MetaData()

hostname = os.getenv('hostname')
database_name = "postgres"
user = "postgres"
password = "mysecretpassword"

Base = declarative_base(metadata=metadata)


class Customers(Base):
    __tablename__ = 'customer_data'
    name = Column(Text)
    country = Column(Text, nullable=False)
    phone = Column(Text, primary_key=True)
    email = Column(Text)

    def __init__(self, name, country, phone, email):
        self.name = name
        self.country = country
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"{self.name},{self.country},{self.phone},{self.email}"


class Subs(Base):
    __tablename__ = 'subscribers_data'
    name = Column(Text)
    country = Column(Text, nullable=False)
    phone = Column(Text, primary_key=True)
    email = Column(Text)

    def __init__(self, name,  country, phone, email):
        self.name = name
        self.country = country
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"{self.name},{self.country},{self.phone},{self.email}"


class Exchange(Base):
    __tablename__ = 'exchange_location'
    name = Column(Text)
    country = Column(Text, nullable=False)
    phone = Column(Text, primary_key=True)
    email = Column(Text)

    def __init__(self, name, country, phone, email):
        self.name = name
        self.country = country
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"{self.name},{self.country},{self.phone},{self.email}"


class Conflict(Base):
    __tablename__ = 'conflict_tickets'
    name = Column(Text)
    country = Column(Text, nullable=False)
    phone = Column(Text, primary_key=True)
    email = Column(Text)

    def __init__(self, name,  country, phone, email):
        self.name = name
        self.country = country
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"{self.name},{self.country},{self.phone},{self.email}"
