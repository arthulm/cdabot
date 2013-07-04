#!/usr/bin/python
# -*- coding: utf-8 -*-

# ::: any function in this script will get the following arguments:
# usermask
# messagetype
# channel
# chatline
# args

# ::: and return a tuple containing the following objects:
# ircmessage (what to send to the IRC channel)
# ttymessage (what to send to the TTY output of the ircbot script)

# you should use the "hallo" function as a template

# note: there is no need to restart the bot if you add functions here,
# the will be reflected just when you save this file.

def hallo(usermask,messagetype,channel,chatline,args):
  ircmessage = "hallo " + usermask.split('!')[0]
  ttymessage = "message sent"
  return ircmessage, ttymessage

def ping(usermask,messagetype,channel,chatline,args):
  ircmessage = usermask.split('!')[0] + ': ' + 'pong'
  ttymessage = "message sent"
  return ircmessage, ttymessage

def analkuh(usermask,messagetype,channel,chatline,args):
  if args == None or len(str(args)) == 0:
    ircmessage = usermask.split('!')[0] + ': ' + '*Kuhherde in die Rektalöffnung treib* MUUUUUUUUUUUUUUH' 
    ttymessage = "message sent"
  else:
    ircmessage = args + ': ' + 'muuuuuuuuuuuuuuuuuuuuuuuuuuuuh *' + args + ' mal eine Kuhherde in die Rektalöffnung treib*'
    ttymessage = "message sent"
  return ircmessage, ttymessage

def poettering(usermask,messagetype,channel,chatline,args):
  ircmessage = 'POETTERIIIIIIIIIIIING!!11111 http://krypton.darkbyte.org/poetteringloveseverybody.mp3'
  ttymessage = "message sent"
  return ircmessage, ttymessage

def penis(usermask,messagetype,channel,chatline,args):
  from random import choice
  l = ['EWIGE PENISKRAFT!!!', '8======D', '8===============D', 'WEEEEENIS', 'PR0NPENIX', 'Wahre Männer benutzen XXXL Kondome!', 'Für mehr pr0n auf dem Beamer!', 'PENIS!!!!!!!!!!!11111', 'Pimmel!', 'http://de.wikipedia.org/wiki/Penis']
  m = choice(l)
  ircmessage = usermask.split('!')[0] + ': ' + m
  ttymessage = "message sent"
  return ircmessage, ttymessage

def whatnext(usermask,messagetype,channel,chatline,args):
  ircmessage = None
  ttymessage = "message sent"
  return ircmessage, ttymessage

def dice(usermask,messagetype,channel,chatline,args):
  import random
  num = random.randint(1,6)
  ircmessage = usermask.split('!')[0] + ': ' + str(num)
  ttymessage = "message sent"
  return ircmessage, ttymessage

def weather(usermask,messagetype,channel,chatline,args):
  from weather import weather
  w = weather.weather()
  ircmessage = usermask.split('!')[0] + ", the current weather is: " + w
  ttymessage = "message sent"
  return ircmessage, ttymessage

def twitter(usermask,messagetype,channel,chatline,args):
  allowed_usermasks = ['armin@neon.darkbyte.org','armin@xenon.darkbyte.org']
  if args == None:
    ircmessage = "refusing to make an empty tweet"
    ttymessage = "did not tweet anything"
  else:
    allowed = False
    for mask in allowed_usermasks:
      if mask in usermask:
        allowed = True
    if not allowed == True:
      ircmessage = usermask.split('!')[0] + ": i can not do this, dave."
      ttymessage = "twitter: users mask was not in the list of allowed usermasks."
    else:
      from twitter import twitter
      try:
        twitter.update_status(str(args))
        ircmessage = usermask.split('!')[0] + ": tweet sent: " + str(args)
        ttymessage = "tweet should have been sent."
      except:
        ircmessage = usermask.split('!')[0] + ": something went wrong when trying to tweet."
        ttymessage = "tweet not sent. something went wrong."
  return ircmessage, ttymessage


if __name__ == '__main__':
  print "This file should not be run stand-alone"
