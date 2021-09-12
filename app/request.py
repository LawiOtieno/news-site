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



def get_news():
    """
    Function that gets the json response to our url request
    """
    get_news_url ='https://newsapi.org/v2/top-headlines/sources?apiKey={NEWS_API_KEY}'
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
    return news_results