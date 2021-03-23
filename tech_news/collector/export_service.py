# flake8: noqa

import requests
import parsel
from requests.exceptions import HTTPError

available_extensions = ("csv", "json")
exported_directory = "/Users/brunobatista/Trybe/projetos_da_trybe/01-projetos-originais-cs/sd-0x-tech-news/tech_news/collector/"

URL_BASE = "https://www.tecmundo.com.br/novidades"

URL_SELECTOR = "h3.tec--card__title > a::attr(href)"

TITLE_SELECTOR = "#js-article-title::text"

TIMESTAMP_SELECTOR = "#js-article-date::attr(datetime)"

WRITER_SELECTOR = "a.tec--author__info__link::text"
# not done
SHARES_COUNT = "#js-comments-btn::attr(data-count)"

COMMENTS_COUNT = "#js-comments-btn::attr(data-count)"
# not done
SUMARRY_SELECTOR = "#js-comments-btn::attr(data-count)"

SOURCES_SELECTOR = "div.z--mb-16 > div a.tec--badge::text"

CATEGORIES_SELECTOR = "#js-categories > a::text"

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

def check_extension(string):
    if not string.endswith('.csv'):
        raise ValueError('Formato invalido')


def get_fields(file_headers, field):
    fields = []
    for header in file_headers:
        fields.append(header[field])
    return fields


def check_headers(file_headers, err_message):
    fields = get_fields(headers, file_headers)
    if file_headers != fields:
        raise ValueError(err_message)


def file_not_found(path):
    file = path.split("/").pop()

    return "Arquivo {} não encontrado".format(file)
