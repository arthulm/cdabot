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

def _usermask_to_username(usermask):
  """A helper function that parses the username out of a usermask"""
  return usermask.split('!')[0]


def hallo(usermask,messagetype,channel,chatline,args):
  ircmessage = "hallo " + _usermask_to_username(usermask)
  ttymessage = "message sent"
  return ircmessage, ttymessage

def ping(usermask,messagetype,channel,chatline,args):
  ircmessage = _usermask_to_username(usermask) + ': ' + 'pong'
  ttymessage = "message sent"
  return ircmessage, ttymessage

def analkuh(usermask,messagetype,channel,chatline,args):
  if args == None or len(str(args)) == 0:
    ircmessage = _usermask_to_username(usermask) + ': ' + '*Kuhherde in die Rektalöffnung treib* MUUUUUUUUUUUUUUH' 
    ttymessage = "message sent"
  else:
    ircmessage = args + ': ' + 'muuuuuuuuuuuuuuuuuuuuuuuuuuuuh *' + args + ' mal eine Kuhherde in die Rektalöffnung treib*'
    ttymessage = "message sent"
  return ircmessage, ttymessage

def muh(usermask,messagetype,channel,chatline,args):
  import urllib2
  try:
    urllib2.urlopen('http://mpd.cdark.net/play/mooh',timeout=1)
    ircmessage = 'muuuuh'
    ttymessage = "sound gespielt.."
  except:
    ircmessage = "Sound abspielen geht nicht im Moment. Muss jemand fixen."
    ttymessage = "sound kaputt, fixen."
  return ircmessage, ttymessage

def miau(usermask,messagetype,channel,chatline,args):
  import urllib2
  try:
    urllib2.urlopen('http://mpd.cdark.net/play/miau',timeout=1)
    ircmessage = 'meeeooooowwwww'
    ttymessage = "sound gespielt.."
  except:
    ircmessage = "Sound abspielen geht nicht im Moment. Muss jemand fixen."
    ttymessage = "sound kaputt, fixen."
  return ircmessage, ttymessage

def poettering(usermask,messagetype,channel,chatline,args):
  import urllib2
  try:
    urllib2.urlopen('http://mpd.cdark.net/play/poetterlove2',timeout=1)
    ircmessage = 'SYSTEMD!!!!!!!!!!!!!!'
    ttymessage = "sound gespielt.."
  except:
    ircmessage = "Sound abspielen geht nicht im Moment. Muss jemand fixen."
    ttymessage = "sound kaputt, fixen."
  return ircmessage, ttymessage

def penis(usermask,messagetype,channel,chatline,args):
  from random import choice
  l = ['EWIGE PENISKRAFT!!!', '8======D', '8===============D', 'WEEEEENIS', 'PR0NPENIX', 'Wahre Männer benutzen XXXL Kondome!', 'Für mehr pr0n auf dem Beamer!', 'PENIS!!!!!!!!!!!11111', 'Pimmel!', 'http://de.wikipedia.org/wiki/Penis', 'a Wurstfilm production', 'you\'re so COCK', 'Gepriesen sei der heilige Penis!', 'Wer lang hat, kann lang hängen lassen.']
  m = choice(l)
  if args == None:
    ircmessage = _usermask_to_username(usermask) + ': ' + m
    ttymessage = "message sent"
  else:
    ircmessage = args.rstrip() + ': ' + m
    ttymessage = "message sent"
  return ircmessage, ttymessage

def vagina(usermask,messagetype,channel,chatline,args):
  from random import choice
  l = ['VAGINA!!!', 'http://de.wikipedia.org/wiki/Vagina', 'MUMU', 'Muschisaft!', '16:57:49 [@goto] keonnten wir das bitte noch fuer vaginas machen? ;)', '*schleck*', '<(o)>']
  m = choice(l)
  if args == None:
    ircmessage = _usermask_to_username(usermask) + ': ' + m
    ttymessage = "message sent"
  else:
    ircmessage = args.rstrip() + ': ' + m
    ttymessage = "message sent"
  return ircmessage, ttymessage

def whatnext(usermask,messagetype,channel,chatline,args):
  ircmessage = None
  ttymessage = "message sent"
  return ircmessage, ttymessage

def dice(usermask,messagetype,channel,chatline,args):
  import random
  num = random.randint(1,6)
  ircmessage = _usermask_to_username(usermask) + ': ' + str(num)
  ttymessage = "message sent"
  return ircmessage, ttymessage

def hubel(usermask,messagetype,channel,chatline,args):
  ircmessage = _usermask_to_username(usermask) + ': ' + "HUBEL HUBEL!!!!!!!!!!!11111111111"
  ttymessage = "message sent"
  return ircmessage, ttymessage

def weather(usermask,messagetype,channel,chatline,args):
  from weather import weather
  w = weather.weather()
  ircmessage = _usermask_to_username(usermask) + ": the current weather is: " + w
  ttymessage = "message sent"
  return ircmessage, ttymessage

def calc(usermask,messagetype,channel,chatline,args):
  from calcer import calcer
  reload(calcer)
  z = calcer.calcclass()
  ircmessage, ttymessage = z.worker(usermask,channel,chatline)

  return ircmessage, ttymessage

def mpd(usermask,messagetype,channel,chatline,args):
  from mpd import mpd
  w = mpd.mpdclient()
  z = w.getCurrentlyPlayingSong()
  ircmessage = _usermask_to_username(usermask) + ": the currently playing song is: " + z
  ttymessage = "message sent"
  return ircmessage, ttymessage

def alarm(usermask,messagetype,channel,chatline,args):
  import urllib2
  urllib2.urlopen('http://mpd.cdark.net/play/mooh',timeout=1)
  from alarmclient import alarmclient
  import time
  w = alarmclient.alarmclient()
  w.on()
  ircmessage = _usermask_to_username(usermask) + ": Die Alarmleuchte wurde für 10 Sekunden aktiviert."
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
      ircmessage = _usermask_to_username(usermask) + ": i can not do this, dave."
      ttymessage = "twitter: users mask was not in the list of allowed usermasks."
    else:
      from twitter import twitter
      try:
        twitter.update_status(str(args))
        ircmessage = _usermask_to_username(usermask) + ": tweet sent: " + str(args)
        ttymessage = "tweet should have been sent."
      except:
        ircmessage = _usermask_to_username(usermask) + ": something went wrong when trying to tweet."
        ttymessage = "tweet not sent. something went wrong."
  return ircmessage, ttymessage

if __name__ == '__main__':
  print "This file should not be run stand-alone"

