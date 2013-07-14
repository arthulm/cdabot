#!/usr/bin/python

import pywapi
import string

# get your weather code from:
# http://edg3.co.uk/snippets/weather-location-codes/
### darmstadt:
weather_code="GMXX0020"

def forecast():
  yahoo_result = pywapi.get_weather_from_yahoo(weather_code)
  del yahoo_result['forecasts'][0]
  text = ""
  for forecast in yahoo_result['forecasts']:
    text += "%s: %s %sC | " % (forecast['day'],string.lower(forecast['text']),forecast['high'])

  return text

if __name__ == '__main__':
  print forecast()

