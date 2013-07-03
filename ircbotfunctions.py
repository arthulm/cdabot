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

def weather(usermask,messagetype,channel,chatline,args):
  from weather import weather
  w = weather.weather()
  ircmessage = usermask.split('!')[0] + ", the current weather is: " + w
  ttymessage = "message sent"
  return ircmessage, ttymessage

def twitter(usermask,messagetype,channel,chatline,args):
  if args == None:
    ircmessage = "refusing to make an empty tweet"
    ttymessage = "did not tweet anything"
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



