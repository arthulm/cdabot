#!/usr/bin/python
# -*- coding: utf-8 -*-

def alarm():
  from alarmclient import alarmclient
  w = alarmclient.alarmclient()
  ircmessage = "Die Alarmleuchte wurde für 3 Sekunden aktiviert."
  return ircmessage

print alarm()


