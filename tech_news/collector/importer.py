# flake8: noqa

from tech_news.collector.importer_service import (
    check_extension,
    check_field,
    check_headers,
    check_url,
    file_not_found,
)

import csv

import json

def csv_importer(filepath):
    check_extension(filepath)
    try: 
        with open(filepath) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=";")
            check_headers(csv_reader.fieldnames, "Cabeçalho inválido")
            data = []
            urls = []
            for line, csv_row in enumerate(csv_reader):
                for field in csv_row:
                    url = csv_row["url"]
                urls.append(url)
                data.append(csv_row)

    except(FileNotFoundError):
        raise ValueError(file_not_found(filepath))

    else:
        return data