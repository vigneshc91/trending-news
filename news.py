from newsapi import NewsApiClient
from constants import Constants

class News:

    def __init__(self):
        self.newsapi = NewsApiClient(api_key=Constants.API_KEY)

    def getHeadlines(self, param):
        params = {
            'language': 'en',
            'category': '',
            'country': '',
            'q': '',
            'sources' : ''
        }
        if 'category' in param:
            params['category'] = param['category'] if param['category'] in Constants.CATEGORIES else ''
        if 'country' in param:
            params['country'] = param['country']
        if 'q' in param:
            params['q'] = param['q']
        
        top_headlines = self.newsapi.get_top_headlines(
            q=params['q'],
            sources=params['sources'],
            category=params['category'],
            language=params['language'],
            country=params['country']
        )

        return top_headlines
