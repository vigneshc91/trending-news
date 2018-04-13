import pycountry

class Constants:
    API_KEY = 'ace5d4f3d2014c4696827b150bd6e982'
    CATEGORIES = [
        'business',
        'entertainment',
        'general',
        'health',
        'science',
        'sports',
        'technology'
    ]
    COUNTRIES = mapping = {country.name: country.alpha_2 for country in pycountry.countries}
    ALEXA_SKILL_ID = 'amzn1.ask.skill.b945408c-db12-45eb-abe7-750c3103b2fa'
    