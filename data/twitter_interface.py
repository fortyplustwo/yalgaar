from twython import Twython, TwythonStreamer
from settings import APP_KEY, ACCESS_TOKEN

class YalgaarTwitterInterface:
    '''gets the data out from Twitter and caches it'''
    
    hashtag = '#SaveTheInternet'
    t = None
    limit = 100 #The number of tweets we will collect

    def __init__(self, hashtag = None, limit = 50):
        '''
        :hashtag: the hashtag for searching
        '''

        if hashtag:
            self.hashtag = hashtag
        
        self.limit = limit

        self.t = Twython(APP_KEY, access_token=ACCESS_TOKEN)
        
    def get_data(self):

        results = self.t.cursor(self.t.search,
                    q           = self.hashtag,
                    count       = (self.limit + 100) #this is random
                    result_type = 'mixed'
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
