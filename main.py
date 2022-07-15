from loguru import logger
import requests
import json


def request_v2(item: str) -> dict:
    '''Примет строку с человеческим запросом. Вернет отчет по записи из ручки v2.'''
    link = 'http://exactmatch-common.wbxsearch-internal.svc.k8s.wbxsearch-dp/v2/search?'
    query = {"query": item.replace(')', '').replace('(', '')}

    with requests.session() as session:
        session.headers['User-Agent'] = 'insomnia/2022.2.1'
        response = session.get(link, params=query)
        result = json.loads(response.text)
    return result


def check_logs():
    pass


def read_file() -> list:
    with open('new_logs.txt', 'r', encoding='utf-8') as file_input:
        logs = file_input.readlines()
    return logs


def main():
    read_file()
    check_logs()


if __name__ == '__main__':
    logger.add('logs.log')
    main()
