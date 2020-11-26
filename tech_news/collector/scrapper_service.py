import requests
import parsel
from requests.exceptions import HTTPError
from os import path

URL_BASE = "https://www.tecmundo.com.br/novidades"

URL_SELECTOR = "h3.tec--card__title > a::attr(href)"

TITLE_SELECTOR = "#js-article-title::text"

TIMESTAMP_SELECTOR = "#js-article-date::attr(datetime)"

WRITER_SELECTOR = "a.tec--author__info__link::text"
# not done
SHARES_COUNT = ".tec--toolbar div:first_child::text"

COMMENTS_COUNT = "#js-comments-btn::attr(data-count)"

SUMARRY_SELECTOR = ".tec--article__body > p:first_child *::text"

SOURCES_SELECTOR = "div.z--mb-16 > div a.tec--badge::text"

CATEGORIES_SELECTOR = "#js-categories > a::text"

# conferir com o cássio qual o melhor tipo de dado
headers = [
    {"name": "url", "selector": URL_SELECTOR},
    {"name": "title", "selector": TITLE_SELECTOR},
    {"name": "timestamp", "selector": TIMESTAMP_SELECTOR},
    {"name": "writer", "selector": WRITER_SELECTOR},
    {"name": "shares_count", "selector": SHARES_COUNT},
    {"name": "comments_count", "selector": COMMENTS_COUNT},
    {"name": "summary", "selector": SUMARRY_SELECTOR},
    {"name": "sources", "selector": SOURCES_SELECTOR},
    {"name": "categories", "selector": CATEGORIES_SELECTOR}
]

def get_urls(content):
    selector = parsel.Selector(content)

    return selector.css(URL_SELECTOR).getall()

def get_news(content, url):
    selector = parsel.Selector(content)

    obj = {"url": url}

    for element in headers:
        field = element["name"]
        if field != "url":
            if field == "shares_count":
                element_data = selector.css(element["selector"]).re(r"\d+")
            else:
                element_data = selector.css(element["selector"]).getall()
            if len(element_data) == 1 and field not in ['categories', 'sources']:
                if field in ['shares_count', 'comments_count']:
                   obj[field] = int(element_data[0])
                else:  
                   obj[field] = element_data[0]
            elif len(element_data) == 0:
                obj = {}
                break
            else:
                obj[field] = element_data

    return obj

def get_next_page_url(content):
    selector = parsel.Selector(content)
    return selector.css(URL_NEXT_PAGE).get()