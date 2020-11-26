# flake8: noqa

from tech_news.database import search_news


def get_news_list(query):
    news_list = []
    news = search_news(query)
    for each in news:
        new =  (each["title"], each["url"])
        news_list.append(new)
    return news_list
