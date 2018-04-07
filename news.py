from newsapi import NewsApiClient
from constants import Constants

class News:

    def __init__(self):
        self.newsapi = NewsApiClient(api_key=Constants.API_KEY)

    def getHeadlines(self, param):
        params = {
            'language': 'en'
        }
        if 'category' in param:
            params['category'] = param['cateogry']
        if 'country' in param:
            params['country'] = param['country']
        if 'q' in param:
            params['q'] = param['q']
        
        top_headlines = self.newsapi.get_top_headlines(params)

        return top_headlines
