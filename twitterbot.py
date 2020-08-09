import tweepy
from abc import ABC, abstractmethod


class PersonalBot(ABC):

    def __init__(self, keys: dict):
        self.auth = tweepy.OAuthHandler(keys['api_key'], keys['api_secret_key'])
        self.auth.set_access_token(keys['access_token'], keys['access_token_secret'])

        self.api = tweepy.API(self.auth)

        self.user = self.api.me()
        print(f'username: {self.user.name}')

        self.label_texts = ['Search', 'Number of Tweets', 'Response', 'Reply', 'Retweet', 'favorite', 'Follow']
        self.answers = {key: '' for key in self.label_texts}

    def main_function(self):
        self.retrieve_entries()

        try:
            number_of_tweets = int(self.answers['Number of Tweets'])
        except ValueError:
            print("'Number of Tweets' needs to be a small natural number")
            return

        for tweet in tweepy.Cursor(self.api.search, self.answers['Search']).items(number_of_tweets):
            print('\nTweet by: @' + tweet.user.screen_name)
            print('ID: @' + str(tweet.user.id))

            try:
                if self.answers['Retweet']:
                    self.retweet_tweet(tweet)
                if self.answers['favorite']:
                    self.favorite_tweet(tweet)
                if self.answers['Reply']:
                    self.reply_tweet(tweet, self.answers['Response'], self.api)
                if self.answers['Follow']:
                    self.follow_tweeter(tweet)
            except StopIteration:
                break

            if self.answers['Reply']:
                try:
                    phrase = self.answers['Response']
                    tweet_id = tweet.user.id
                    username = tweet.user.screen_name
                    self.api.update_status("@" + username + " " + phrase, in_reply_to_status_id=tweet_id)
                    print("Replied with " + phrase)
                except tweepy.TweepError as e:
                    print(e.reason)
                except StopIteration:
                    break

    @staticmethod
    def retweet_tweet(tweet):
        try:
            tweet.retweet()
            print('retweeted')
        except tweepy.TweepError as e:
            print('failed to retweet')
            print(e.reason)

    @staticmethod
    def favorite_tweet(tweet):
        try:
            tweet.favorite()
            print('favorited')
        except tweepy.TweepError as e:
            print('failed to favorite')
            print(e.reason)

    @staticmethod
    def reply_tweet(tweet, phrase, api):
        try:
            tweet_id = tweet.user.id
            username = tweet.user.screen_name
            api.update_status("@" + username + " " + phrase, in_reply_to_status_id=tweet_id)
            print("Replied with " + phrase)
        except tweepy.TweepError as e:
            print(e.reason)

    @staticmethod
    def follow_tweeter(tweet):
        try:
            tweet.user.follow()
            print('Followed user ' + tweet.user.screen_name)
        except tweepy.TweepError as e:
            print('failed to follow user')
            print(e.reason)

    @abstractmethod
    def retrieve_entries(self):
        pass
