import tweepy
import tkinter
import json


class PersonalBot:

    def __init__(self, keys='keys.json'):
        with open(keys, 'r') as f:
            self.keys = json.load(f)

        self.auth = tweepy.OAuthHandler(self.keys['api_key'], self.keys['api_secret_key'])
        self.auth.set_access_token(self.keys['access_token'], self.keys['access_token_secret'])

        self.api = tweepy.API(self.auth)

        self.user = self.api.me()
        print(self.user.name)

    def follow_followers(self):
        for follower in tweepy.Cursor(self.api.followers).items():

            try:
                follower.follow()
                print(f'followed {follower.name}')
            except tweepy.error.TweepError as e:
                print(e.reason)
                print(f'failed to follow {follower.name}')

    def main_function(self):
        pass


def main():
    my_bot = PersonalBot()


if __name__ == '__main__':
    main()
