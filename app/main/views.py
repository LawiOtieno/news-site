from ..request import get_news,get_articles
from flask import render_template,request,redirect,url_for
from . import main



#Views
@main.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    current_news = get_news()
    print(current_news)
    title = "Welcome to the Best News Website for latest and current news"
    return render_template('index.html', title= title, current_news = current_news )

@main.route("/news/<news_id>")
def articles(news_id):
    """
    view news page function that returns the news detail page and its data from a source
    """
    #get news based on source id
    articles = get_articles(news_id)
    print(articles)
    title = f'{news_id}'
    return render_template("articles.html", articles = articles, title = title)