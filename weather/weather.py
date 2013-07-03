#!/usr/bin/python

import pywapi
import string

# get your weather code from:
# http://edg3.co.uk/snippets/weather-location-codes/
### darmstadt:
weather_code="GMXX0020"

def weather():
  yahoo_result = pywapi.get_weather_from_yahoo(weather_code)
  text = string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "C"
  return text

if __name__ == '__main__':
  print weather()

