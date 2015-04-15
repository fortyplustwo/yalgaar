from flask.ext.frozen import Freezer
from yalgaar.yalgaar import app
from yalgaar.data.collect_tweets import collect_tweets

f = Freezer(app)

if __name__ == '__main__':
    #first get fresh tweets
    collect_tweets(tweet_type = 'recent', hashtag = '#SaveTheInternet', limit = 100)
    collect_tweets(tweet_type = 'popular', hashtag = '#SaveTheInternet', limit = 100)

    #now freeze them!
    f.freeze()

