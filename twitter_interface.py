from twython import Twython, TwythonStreamer
from settings import APP_KEY, ACCESS_TOKEN


class YalgaarTwitterInterface:
    '''gets the data out from Twitter and caches it'''
    
    hashtag = '#SaveTheInternet'
    t = None

    def __init__(self, hashtag = None):
        '''
        :hashtag: the hashtag for searching
        '''

        if hashtag:
            self.hashtag = hashtag
        
        self.t = Twython(APP_KEY, access_token=ACCESS_TOKEN)
        
    def get_data(self):

        results = self.t.search_gen(
                    self.hashtag,
                    count       = 100, 
                    result_type =  'mixed'
                    )
    
        try:
            for r in results:
                print r['text']

            return results
        except Exception as e:
            raise e
            return False


y = YalgaarTwitterInterface()
y.get_data()
