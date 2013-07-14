#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import datetime

db_file='/home/bot/cdabot/calcer/calc.db'

class calcclass(object):

  def __init__(self):
    self.connection = sqlite3.connect(db_file)
    self.cursor = self.connection.cursor()

  def moo(self,args):
    self.result = "ficken"
    return self.result

  def test(self,args):
    args2 = "JO2"
    return args2

  def getCalc(self,calcname):
    prepared_statement = '''select * from calc where key = ?'''
    try:
      self.cursor.execute(prepared_statement, [(calcname)])
      result = self.cursor.fetchall()
    except:
      result = "sowas kenne ich nicht."
    return result

  def addCalc(self,key,value,nickname):
    time = datetime.datetime.isoformat(datetime.datetime.now())
    values = (key,value,nickname,time)
    print str(values)
    prepared_statement = "insert into calc (key, value, nickname, time) values (?,?,?,?)"
    try:
        self.cursor.execute(prepared_statement, values)
        self.connection.commit()
        return True
    except sqlite3.IntegrityError:
        return str(sys.exc_info())
    except:
        return str(sys.exc_info())

  def getTimeString(self,timestamp):
    print "--------------- " + timestamp
    t = timestamp.replace('T',' ')
    t = t.split('.')[0]
    timestring = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
    return timestring
  

  def closeConnection(self):
    self.cursor.close()



def formatChatline(result):
  key, value, nickname, time = result
  chatline = "%s = %s (added by: %s, %s)" % (key, value, nickname, getTimeString(time))
  return chatline




