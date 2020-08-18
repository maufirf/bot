import os
import json
import facebook
import tweepy
import stringer
import datetime
from censoring import censor

print('IMPORT FINISHED')

ENV = None
if os.path.exists('auth.json'):
    ENV_FILE = open('auth.json')
    ENV = json.load(ENV_FILE)
    ENV_FILE.close()
else:
    ENV = {
        "FB_ACC_TOKEN_PAINTMIN":os.environ.get('FB_ACC_TOKEN_PAINTMIN'),
        "PAGE_ID":os.environ.get('PAGE_ID'),
        "TWITTER_CONSUMER_KEY":os.environ.get('TWITTER_CONSUMER_KEY'),
        "TWITTER_CONSUMER_SECRET":os.environ.get('TWITTER_CONSUMER_SECRET'),
        "TWITTER_ACC_TOKEN":os.environ.get('TWITTER_ACC_TOKEN'),
        "TWITTER_ACC_TOKEN_SECRET":os.environ.get('TWITTER_ACC_TOKEN_SECRET'),
    }
print('TOKEN LOADED')

with open('emojis.json','r',encoding='UTF-8') as emojis_file:
    emojis = json.load(emojis_file)
print('EMOJI SET LOADED:',emojis)

stringer_ctrl = stringer.Stringer_Ctrl()
print('STRINGER OBJECT INITIALIZED')
emoji_selected = emojis[datetime.datetime.now().hour]
generated = stringer_ctrl.generate([emoji_selected+'{0}'+emoji_selected, 1])
print(f'NEW TEXT GENERATED: {generated}')

# hard censoring
generated = censor(generated)
print(f'POST-CENSORING TEXT: {generated}')

graph = facebook.GraphAPI(access_token=ENV['FB_ACC_TOKEN_PAINTMIN'])
print('FACEBOOK GRAPH OBJECT CREATED',graph,sep='\n')

auth = tweepy.OAuthHandler(ENV["TWITTER_CONSUMER_KEY"], ENV["TWITTER_CONSUMER_SECRET"])
auth.set_access_token(ENV["TWITTER_ACC_TOKEN"], ENV["TWITTER_ACC_TOKEN_SECRET"])
api = tweepy.API(auth)
print('TWITTER API OBJECT CREATED',api,sep='\n')

fb_response = graph.put_object(parent_object='me', connection_name='feed',
                  message=generated)
print('FACEBOOK RESPONSE: ',fb_response,sep='\n')

twitter_response = api.update_status(generated)
print('TWITTER RESPONSE: ',twitter_response,sep='\n')