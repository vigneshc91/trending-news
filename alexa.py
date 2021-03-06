from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from news import News
from constants import Constants
from langdetect import detect
from googletrans import Translator
import json
import logging

app = Flask(__name__)
ask = Ask(app, '/')
app.config['ASK_APPLICATION_ID'] = Constants.ALEXA_SKILL_ID
news = News()
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@app.route('/')
def index():
    return 'welcome to Trending News.'

@ask.launch
def launched():
    text = render_template('welcome')
    return question(text)

@ask.intent('AMAZON.HelpIntent')
def help():
    text = render_template('help')
    return question(text)

@ask.intent('AMAZON.CancelIntent')
@ask.intent('AMAZON.StopIntent')
def stop():
    text = render_template('cancel')
    return statement(text)

@ask.intent('TrendingNewsIntent')
def trendingNews(country, category):
    params = {}
    if country is not None:
        params['country'] = country
    if category is not None:
        params['category'] = category

    headlines = news.getHeadlines(params)
    if headlines['totalResults'] > 0:
        session.attributes['news'] = headlines
        session.attributes['total'] = len(headlines['articles'])
        session.attributes['current'] = 0

        text = headlines['articles'][0]['title']
        description = json.loads(json.dumps(headlines['articles'][0]))['description']
        if detect(text) != 'en':
            translator = Translator()
            text = headlines['articles'][0]['title'] = translator.translate(text).text
        if description is not None and detect(description) != 'en':
            description = ''
        response = render_template('news', source=headlines['articles'][0]['source']['name'], news=text)
        return question(response).simple_card(title=text, content=description)
    else:
        response = render_template('no_results')
        return question(response)

@ask.intent('DetailIntent')
def readMoreAboutNews():
    if 'news' in session.attributes:
        description = json.loads(json.dumps(session.attributes['news']['articles'][session.attributes['current']]))['description']
        print(description)
        if description is None:
            response = render_template('description_error')
        elif detect(description) != 'en':
            translator = Translator()
            description = session.attributes['news']['articles'][session.attributes['current']]['description'] = translator.translate(description).text
            response = description + '. Do you want to read the next or previous news.'
        else:
            description = session.attributes['news']['articles'][session.attributes['current']]['description']
            response = description + '. Do you want to read the next or previous news.'
    else:
        response = render_template('detail_news_error')
    return question(response)

@ask.intent('AMAZON.NextIntent')
def readNextNewsIntent():
    if 'news' in session.attributes:
        if session.attributes['current'] < session.attributes['news']['totalResults'] :
            session.attributes['current'] += 1
            headlines = session.attributes['news']
            
            text = headlines['articles'][session.attributes['current']]['title']
            description = headlines['articles'][session.attributes['current']]['description']
            if text is not 'null' and detect(text) != 'en':
                translator = Translator()
                text = headlines['articles'][session.attributes['current']]['title'] = translator.translate(text).text
            if description is not None and detect(description) != 'en':
                description = ''
            response = render_template('news', source=headlines['articles'][session.attributes['current']]['source']['name'], news=text)

            return question(response).simple_card(title=text, content=description)
        else:
            response = render_template('not_having_further_news')
    else:
        response = render_template('next_news_error')
    return question(response)
    
@ask.intent('AMAZON.PreviousIntent')
def readPreviousNewsIntent():
    if 'news' in session.attributes:
        if session.attributes['current'] > 0 :
            session.attributes['current'] -= 1
            headlines = session.attributes['news']

            text = headlines['articles'][session.attributes['current']]['title']
            description = headlines['articles'][session.attributes['current']]['description']
            if description is not None and detect(description) != 'en':
                description = ''
            response = render_template('news', source=headlines['articles'][session.attributes['current']]['source']['name'], news=text)
            return question(response).simple_card(title=text, content=description)
        else :
            response = render_template('not_having_previous_news')
    else:
        response = render_template('previous_news_error')
    return question(response)

@ask.intent('ListCategoryIntent')
def listCategoryIntent():
    response = render_template('categories_list', categories= ', '.join(Constants.CATEGORIES))
    return question(response)

if __name__ == '__main__':
    app.run(debug=True)
