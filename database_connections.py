#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:04:04 2023

@author: gowrav
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from sqlalchemy import Column, MetaData, Text, Integer
from sqlalchemy.ext.declarative import declarative_base

metadata = Metadata()

hostname = "localhost"
database_name = "customers"
user = "postgres"
password = None


class SQL:

    def __init__(self, **kwargs):
        self.engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{hostname}:5432/{database_name}')
        self.sessionfactory = sessionmaker(bind=self.engine)

    def transaction(self):
        session = scoped_session(self.sessionfactory)
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


Base = declarative_base(metadata=metadata)


class Customers(Base):

    __tablename__ = 'customer_data'
    name = Column(Text, nullable=False)
    age = Column(Integer, nullable=False)
    country = Column(Text, nullable=False)

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def __repr__(self):
        return f"{self.name},{self.age},{self.country}"
