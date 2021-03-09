import requests
from time import sleep
from parsel import Selector

BASE_URL = "https://www.tecmundo.com.br/novidades"


def get_next_page(number_page):
    response = requests.get(f"{BASE_URL}?page={number_page}")
    return Selector(text=response.text)


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        sleep(delay)
        return ""
    else:
        sleep(delay)
        return response.text


def verify_has_integer(data):
    if data and data.strip() != '':
        return int(data.split()[0])

    return 0


def extract_information(url):
    response = fetch_content(url=url)
    news_selector = Selector(text=response)
    return {
        "url": url,
        "title": news_selector.css(
            "h1.tec--article__header__title::text"
        ).get(),
        "timestamp": news_selector.css(
            "time::attr(datetime)"
        ).get(),
        "writer": news_selector.css("a.tec--author__info__link::text").get(),
        "shares_count": verify_has_integer(
            news_selector.css(
                "nav.tec--toolbar > div.tec--toolbar__item::text"
            ).get()
        ),
        "comments_count": verify_has_integer(
            news_selector.css("button#js-comments-btn::attr(data-count)").get()
        ),
        "summary": news_selector.css(".tec--article__body p *::text").get(),
        "sources": news_selector.css("div a.tec--badge::text").getall(),
        "categories": news_selector.css("div#js-categories a.tec--badge tec--badge--primary::text").getall(),
    }


def scrape(fetcher, pages=1):
    arr_news_information = []
    next_page = 1

    while next_page <= pages:
        news_selector = get_next_page(next_page)
        news_list_items = news_selector.css(".tec--list__item")

        for item in news_list_items:
            page_url = item.css("a.tec--card__thumb__link::attr(href)").get()
            arr_news_information.append(extract_information(page_url))

        next_page += 1

    return arr_news_information
