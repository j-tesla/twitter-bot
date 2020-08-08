import tweepy
import tkinter
import json

with open('keys.json', 'r') as f:
    keys = json.load(f)

auth = tweepy.OAuthHandler(keys['api_key'], keys['api_secret_key'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])

api = tweepy.API(auth)

user = api.me()

print(user.name)

for follower in tweepy.Cursor(api.followers).items():

    try:
        follower.follow()
        print(f'followed {follower.name}')
    except tweepy.error.TweepError:
        print(f'failed to follow {follower.name}')
