import requests
from constants import Constants

class News:

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
            params['country'] = Constants.COUNTRIES[param['country']] if param['country'] in Constants.COUNTRIES else param['country']
        if 'q' in param:
            params['q'] = param['q']
        
        headers = {'Authorization': 'Bearer '+Constants.API_KEY}
        
        top_headlines = requests.get(url=Constants.URL, params=params, headers=headers).json()
        
        return top_headlines
