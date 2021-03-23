# flake8: noqa

import requests
import parsel
from requests.exceptions import HTTPError
from tech_news.collector.scrapper_service import (
    get_urls,
    get_news
)
from pathlib import Path

from time import sleep 
from tech_news.database import insert_or_update

URL_BASE = "https://www.tecmundo.com.br/novidades"

def fetch_content(url, timeout=3, delay=0.5):
    try:
        sleep(delay)
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError) as http_error:
        return ""
    else:
        return response.text


def scrape(fetcher=fetch_content, pages=1):
    current_page = 1

    news_data = []

    while current_page <= pages:
        content_news = fetcher(URL_BASE + "?page=" + str(pages))
        
        urls = get_urls(content_news)

        for url in urls:
            content_details = fetcher(url)
            news = get_news(content_details, url) 
            if news:
                news_data.append(news)
                
        current_page += 1
    return news_data