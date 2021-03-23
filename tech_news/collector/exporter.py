# flake8: noqa

from tech_news.collector.export_service import (
    exported_directory,
    headers,
    check_extension,
    file_not_found,
    check_headers 
)

from tech_news.database import find_news

import csv

import json
import sys

def csv_exporter(file_path):
    data = find_news()

    try:
        check_extension(file_path)

        write_in_file(file_path, data)

    except ValueError:
        raise ValueError('Formato invalido')

def write_in_file(file_path, all_news):
    with open(file_path, mode="w") as csv_file:

        csv_columns = all_news[0].keys()

        writer = csv.DictWriter(
            csv_file, fieldnames=csv_columns, delimiter=";"
        )
        writer.writeheader()
        for line in all_news:
            line["sources"] = ",".join(line["sources"])
            line["categories"] = ",".join(line["categories"])
            writer.writerow(line)
            
# ver que vai ser mais um regra do requisito de ir no banco e buscar noticia
