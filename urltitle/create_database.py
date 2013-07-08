#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import datetime

con = lite.connect('test.db')

def create_table():
  with con:
      cur = con.cursor()    
      cur.execute("CREATE TABLE urls(url TEXT, usermask TEXT, channel TEXT, time)")

def insert_test_row():
  with con:
    cur = con.cursor()
    date = datetime.datetime.now().isoformat()
    print date
    cur.execute('INSERT INTO urls VALUES (?,?,?,?)', ('foo', 'bar', 'baz', date))

def show_table():
  with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM urls")
    a = cur.fetchall()
    return a

if __name__ == '__main__':
#  create_table()
  insert_test_row()
  print show_table()




