import os


class Config:
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

    
config_options = {
'development':DevConfig,
'production':ProdConfig
}