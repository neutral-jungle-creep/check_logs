from loguru import logger
from urllib.request import urlopen
import requests
import json


def request_v2(item: str) -> dict:
    '''Примет строку с человеческим запросом. Вернет отчет по записи из ручки v2.'''
    link = 'http://exactmatch-common.wbxsearch-internal.svc.k8s.wbxsearch-dp/v2/search?'
    query = {"query": item}

    with requests.session() as session:
        session.headers['User-Agent'] = 'insomnia/2022.2.1'
        response = session.get(link, params=query)
        result = json.loads(response.text)
    return result


def check_logs(logs: list):
    link = 'https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search={}'
    for log in logs:
        logger.info(f'Человеческий запрос: {log}')
        link = link.format("+".join([word for word in log.split()]))
        logger.info(f'Ссылка на выдачу: {link}')
        logger.info(f'Результаты ручки экзакта: {request_v2(log)}')


def read_file() -> list[str]:
    with open('new_logs.txt', 'r', encoding='utf-8') as file_input:
        logs = file_input.readlines()
        logger.debug(f'Прочитано {len(logs)} строк из файла.')
    return logs


def main():
    logs = read_file()
    check_logs(logs)


if __name__ == '__main__':
    logger.add('logs.log')
    main()
