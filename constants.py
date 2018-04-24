import pycountry

class Constants:
    URL = 'https://newsapi.org/v2/top-headlines'
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
    COUNTRIES_SUPPORTED = [
        'ae', 'ar', 'at', 'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cu', 'cz', 'de', 'eg', 'fr', 'gb', 'gr', 'hk', 'hu', 'id', 'ie', 'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma', 'mx', 'my', 'ng', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sg', 'si', 'sk', 'th', 'tr', 'tw', 'ua', 'us', 've', 'za'
    ]
    ALEXA_SKILL_ID = 'amzn1.ask.skill.b945408c-db12-45eb-abe7-750c3103b2fa'
    