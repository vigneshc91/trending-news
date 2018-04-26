import requests
from constants import Constants

class News:

    def getHeadlines(self, param):
        params = {
            'category': '',
            'country': 'in',
            'q': ''
        }
        if 'category' in param:
            params['category'] = param['category'] if param['category'] in Constants.CATEGORIES else ''
        if 'country' in param:
            country = Constants.COUNTRIES[param['country'].lower()] if param['country'].lower() in Constants.COUNTRIES else param['country']
            params['country'] = country if country in Constants.COUNTRIES_SUPPORTED else 'in'
        if 'q' in param:
            params['q'] = param['q']
        
        headers = {'Authorization': 'Bearer ' + Constants.API_KEY}
        
        top_headlines = requests.get(url=Constants.URL, params=params, headers=headers).json()
        
        return top_headlines
