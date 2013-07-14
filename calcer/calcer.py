#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import datetime

db_file='/home/bot/cdabot/calcer/calc.db'

class calcclass(object):

  def __init__(self):
    self.connection = sqlite3.connect(db_file)
    self.cursor = self.connection.cursor()

  def formatAnswer(self,answer):
    key = answer[0][0]
    value = answer[0][1]
    nickname = answer[0][2]
    time = answer[0][3].split(".")[0].replace('T',' ')
    text = "* " + key + " = " + value + " (added by: " + nickname + ", " + time + ")"
    return text

  def worker(self,usermask,channel,chatline):
    if "=" in chatline: 
      # request to define a new calc
      rawkey, rawvalue = chatline.split('=', 1)
      key = rawkey[6:].rstrip()
      value = rawvalue.lstrip()
      self.addCalc(key,value,usermask)
      ircmessage = "KEY:" + key + ":::" + "VALUE:" + value + "EOL"
      ttymessage = "new calc requested."
    else:
      # request to get a calc
      requested = chatline[6:]
      answer = self.getCalc(requested)
      if len(answer) == 0:
        ircmessage = requested + " kenne ich nicht."
      else:
        ircmessage = self.formatAnswer(answer)
      ttymessage = "calc requested: " + requested
    return ircmessage, ttymessage

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




