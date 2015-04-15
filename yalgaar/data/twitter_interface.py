from twython import Twython, TwythonStreamer
from settings import APP_KEY, ACCESS_TOKEN

class YalgaarTwitterInterface:
    '''gets the data out from Twitter and caches it'''
    
    hashtag = '#SaveTheInternet'
    t = None
    limit = 100 #The number of tweets we will collect

    def __init__(self, hashtag = None, limit = 50, tweet_type = 'mixed'):
        '''
        :hashtag: the hashtag for searching
        :limit: how many tweets to collect
        :tweet_type: what type of tweet to collect - popular/recent/mixed. See Twitter API docs
        '''

        if hashtag:
            self.hashtag = hashtag
        
        self.limit = limit
        self.tweet_type = tweet_type
        self.t = Twython(APP_KEY, access_token=ACCESS_TOKEN)
        
    def get_data(self):

        results = self.t.cursor(self.t.search,
                    q           = self.hashtag,
                    count       = (self.limit * 2), #this is to so that we have enough tweets which remain even after filters below
                    result_type = self.tweet_type,
                    )
    
        try:
            count = 0
            tweets = {}

            for r in results: #results is a GENERATOR!
                if count >= self.limit:
                    break;

                #filter out these tweets further

                #we don't want anyone's conversations
                #we don't want to snoop on someone's conversations
                if r['in_reply_to_screen_name'] is not None:
                    continue;
                else:
                    tweets[r['text']] = r
                    count = count + 1
            return tweets
        except Exception as e:
            raise e
            return False


if __name__ == '__main__':
    y = YalgaarTwitterInterface()
    y.get_data()
