import os
import json
import facebook
import tweepy
import stringer

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

stringer_ctrl = stringer.Stringer_Ctrl()
print('STRINGER OBJECT INITIALIZED')
generated = stringer_ctrl.generate()
print(f'NEW TEXT GENERATED: {generated}')

graph = facebook.GraphAPI(access_token=ENV['FB_ACC_TOKEN_PAINTMIN'])
print('FACEBOOK GRAPH OBJECT CREATED',graph,sep='\n')

auth = tweepy.OAuthHandler(ENV["TWITTER_CONSUMER_KEY"], ENV["TWITTER_CONSUMER_SECRET"])
auth.set_access_token(ENV["TWITTER_ACC_TOKEN"], ENV["TWITTER_ACC_TOKEN_SECRET"])
api = tweepy.API(auth)
print('TWITTER API OBJECT CREATED',api,sep='\n')

fb_response = graph.put_object(parent_object='me', connection_name='feed',
                  message=stringer_ctrl.generate())
print('FACEBOOK RESPONSE: ',fb_response,sep='\n')

twitter_response = api.update_status(generated)
print('TWITTER RESPONSE: ',twitter_response,sep='\n')