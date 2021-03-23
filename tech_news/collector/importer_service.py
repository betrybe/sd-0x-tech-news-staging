# flake8: noqa

import requests
import parsel
from requests.exceptions import HTTPError
from os import path

import csv

import json
available_extensions = ("csv", "json")

def check_extension(string):
    if not string.endswith('.csv'):
       raise ValueError('Formato invalido')

def check_field(field, line):
    if not field:
        raise ValueError("Erro na notícia {}".format(line))

def get_fields(file_headers, field):
    fields = []
    for header in file_headers:
        fields.append(header[field])
    return fields

def check_headers(file_headers, err_message):
    headers = [
        "url",
        "title",
        "timestamp",
        "writer",
        "shares_count",
        "comments_count",
        "summary",
        "sources",
        "categories"
    ]

    if file_headers != headers:
        raise ValueError("Cabeçalho inválido")

def check_url(urls, url, line):
    if urls.count(url) > 0:
        raise ValueError("Notícia {} duplicada".format(line))

def file_not_found(path):
    file = path.split("/").pop()

    return "Arquivo {} não encontrado".format(file)
