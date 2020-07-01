import tweepy
import json, csv

class Twitter_miner:
    """
    This class allows you to mine data on twitter

    Methods:

    search_yourself ---- gets your tweets
    search_for_user ---- gets tweets of a specific user and displays result in console
    search_for_user_csv ---- gets tweets of a specific user and displays results in a csv file
    search_for_word_csv ---- gets tweets that mention speicific word and display it in a csv file

    """

    def __init__(self, consumer_key, consumer_secret, access_token,
        access_token_secret):

        """
        Atributes of Twitter_minner object:

        consumer_key(str) ---- twitter developer consumer key
        consumer_secret(str) ---- twitter developer consumer secret key
        access_token(str) ---- twitter developer access token
        access_token_secret(str) ---- twitter developer secret access token

        """

        auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        # creating the api object while passing in auth information
        self.api=tweepy.API(auth)

    def search_yourself(self):

        "Searches for your tweets and displayes them in the console"

        public_tweets=self.api.home_timeline()
        for tweet in public_tweets:
            print(tweet.created_at, tweet.text, sep=" ||| ")
            print(tweet.user.name, tweet.user.screen_name, tweet.user.location,
            sep=' ||| ')

    def search_for_user(self, user, numb_pulls):
        """
        Searches for tweets of a specific user and displays them in the console

        args:
        user(string) --- username of the tweeter account
        numb_pulls(int) --- number of tweets to retrieve
        """

        results = self.api.user_timeline(id=user, count=numb_pulls)
        for tweet in results:
           print(tweet.text.encode(encoding='UTF-8',errors='strict'))

    def search_for_user_csv(self, user, numb_pulls, file):
        """
        Searches for tweets of a specific user and displays them in csv file

        args:
        user(string) --- username of the tweeter account
        numb_pulls(int) --- number of tweets to retrieve
        file(str) ---- name of csv file
        """

        results = self.api.user_timeline(id=user, count=numb_pulls)
        with open(file, 'w', encoding='utf-8') as f:
            fieldnames = ['date', 'username', 'statement']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for tweet in results:
                writer.writerow({'date': tweet.created_at,
                'username': tweet.user.screen_name,
                "statement": tweet.text.encode("utf-8")}, )



    def search_for_word_csv(self, word, numb_pulls, file):
        """
        Searches for tweets including a certain word and saves the result in
        a csv file

        args:
        word (str) ---- the word that you are looking for
        numb_pulls (int)----number of tweets to retrieve
        file(str) ------ csv file where the information is going to be stored
        """

        # Calling the user-timeline function with our paramters
        # results = api.user_timeline(id=name, count=tweetCount)
        results = self.api.search(q = word,  lang='en', count=numb_pulls)
        # foreach through all tweets pulled
        with open(file, 'w', encoding='utf-8') as f:
            fieldnames = ['date', 'username', 'statement']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for tweet in results:
                writer.writerow({'date': tweet.created_at,
                'username': tweet.user.screen_name,
                "statement": tweet.text.encode("utf-8")}, )


if __name__ == "__main__":

    miner = Twitter_miner()
    miner.search_for_user_csv('RachelMorris', 20, "tweet7.csv")
