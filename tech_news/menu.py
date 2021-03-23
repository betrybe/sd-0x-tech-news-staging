# flake8: noqa

from tech_news.analyzer.ratings import (top_5_categories, top_5_news)
from tech_news.analyzer.search_engine import (
    search_by_category, search_by_date, search_by_source, search_by_title)
from tech_news.collector.scrapper import (
    scrape, fetch_content)
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.importer import csv_importer
from tech_news.database import create_news
import sys


def collector_menu():
    option = input("Selecione uma das opções a seguir:\n 1 - Importar notícias a partir de um arquivo CSV;\n 2 - Exportar notícias para CSV;\n 3 - Raspar notícias online;\n 4 - Sair.\n")
    if option == '1':
        file_importer = input("Digite o nome do arquivo CSV a ser importado: ")
        data = csv_importer(file_importer)
        create_news(data)
    elif option == '2':
        file_exporter = input("Digite o nome do arquivo CSV a ser exportado: ")
        csv_exporter(file_exporter)
        print('exportado com sucesso!')
    elif option == '3':
        page = input("Digite a quantidade de páginas a serem raspadas: ")
        data = scrape(fetcher=fetch_content, pages=int(page))
        create_news(data)
    elif option == '4':
        print("Encerrando script")
        pass
    else:
        print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    option = input("Selecione uma das opções a seguir:\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n 3 - Buscar notícias por fonte;\n 4 - Buscar notícias por categoria;\n 5 - Listar top 5 notícias;\n 6 - Listar top 5 categorias;\n 7 - Sair.\n")
    if option == '1':
        title = input("Digite o título: ")
        print(search_by_title(title))
    elif option == '2':
        date = input("Digite a data no formato aaaa-mm-dd: ")
        print(search_by_date(date))
    elif option == '3':
        source = input("Digite a fonte: ")
        print(search_by_source(source))
    elif option == '4':
        categoty = input("Digite a categoria: ")
        print(search_by_category(categoty))
    elif option == '5':
        print(top_5_news())
    elif option == '6':
        print(top_5_categories())
    elif option == '7':
        print('Encerrando script')
        pass
    else:
        print("Opção inválida", file=sys.stderr)
