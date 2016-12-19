#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2864707582-6qSeUB0lahZGFeLBJYuwKZ8bWOOEfAcDawSylfC"
access_token_secret = "Na1ABNSFhnGJHBRcLK2F8HG8XkPcSz9SbfbcArBhnIVOq"
consumer_key = "PffAk36v7N1PJ7QiesJ34Klf6"
consumer_secret = "3smwBzONs7QCgugc6wEcFGBEhTDTwBOyaavokXQIUHrKF89M0H"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['emirates'])
    stream.filter(languages=["en"], track=["emirates", "airline_emirates"])