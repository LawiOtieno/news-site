import urllib.request, json
from app.models import News, Articles


#Getting api_key
api_key = None

#Getting the news base_url
base_url = None

#getting articles_base_url 
articles_base_url = None

def configure_request(app):
    global api_key, base_url, articles_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_base_url = app.config['ARTICLES_BASE_URL']