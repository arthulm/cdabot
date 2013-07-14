#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String, DateTime

import datetime

engine = create_engine('sqlite:///calc.db',echo=True)

metadata=MetaData(bind=engine)
main_table=Table('calc',metadata,
            Column('key',String(256),primary_key=True),
            Column('value',String(1024),nullable=False),
            Column('nickname',String(20),nullable=False),
            Column('time',DateTime,nullable=False,default=datetime.datetime.now),
            )

metadata.create_all()


