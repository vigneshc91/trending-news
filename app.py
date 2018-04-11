from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from news import News
from constants import Constants
import logging

app = Flask(__name__)
ask = Ask(app, '/')
news = News()
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@ask.launch
def launched():
    text = render_template('welcome')
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
        if len(country) > 2:
            params['country'] = Constants.COUNTRIES[country]
        else:
            params['country'] = country
    if category is not None:
        params['category'] = category

    headlines = news.getHeadlines(params)
    
    session.attributes['news'] = headlines
    session.attributes['total'] = headlines['totalResults']
    session.attributes['current'] = 0
    
    text = headlines['articles'][0]['title']
    response = render_template('news', source=headlines['articles'][0]['source']['name'], news=text)

    return question(response)

@ask.intent('AMAZON.MoreIntent')
def readMoreAboutNews():
    detail = session.attributes['news']['articles'][session.attributes['current']]['description']
    return question(detail)

@ask.intent('AMAZON.NextIntent')
def readNextNewsIntent():
    session.attributes['current'] += 1
    headlines = session.attributes['news']
    text = headlines['articles'][session.attributes['current']]['title']
    response = render_template('news', source=headlines['articles'][session.attributes['current']]['source']['name'], news=text)

    return question(response)

if __name__ == '__main__':
    app.run(debug=True)
