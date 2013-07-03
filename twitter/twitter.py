#!/usr/bin/python

import oauth2 as oauth
import json
import urlparse
import urllib

CONSUMER_KEY="CuBk94QbGdAddmoVxzzCbA"
CONSUMER_SECRET="DL5nkaW5iI0VDr59ZmlTyAmrWjnONWAoan7tFFxzf8"

ACCESS_KEY = "1558427227-A0dFRlpWJD7oLH7moKG4j2a8cCvD4e6UPNaJYpD"
ACCESS_SECRET = "QodH8cQ7ERPk9SBEibL2phgkqrnF32f37PqYD7zmM"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

def get_timeline():
  timeline_endpoint = "http://api.twitter.com/1.1/statuses/home_timeline.json"
  response, data = client.request(timeline_endpoint)
  tweets = json.loads(data)
  print "get_timeline response: " + str(dir(response))
  # return tweets in json
  return tweets

def get_rate_limit():
  endpoint = "http://api.twitter.com/1.1/application/rate_limit_status.json"
  response, data = client.request(endpoint)
  answer = json.loads(data)
  return str(answer)

def update_status(status):
  body = {'status': status}
  body = urllib.urlencode(body)
  status_endpoint = "http://api.twitter.com/1.1/statuses/update.json"
  response, data = client.request(status_endpoint, method="POST", body=body)
  return data

if __name__ == '__main__':
  print "This is intended to run as a module. Use: update_status('something') to update your status"

