#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:04:04 2023

@author: gowrav
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from sqlalchemy import Column, Metadata,String, Integer
from sqlalchemy.ext.declarative import declarative_base
 


hostname="localhost"
database_name="testload"
user="gowrav"
password=None

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


metadata = Metadata()

Base =  declarative_base(metadata=Metadata)

class Customers(Base):
    __tablename__='customers'
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False )
    country = Column(String, nullable=False )
    
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        
    def __repr__(self):
        return f"{self.name},{self.age},{self.country}"
                        