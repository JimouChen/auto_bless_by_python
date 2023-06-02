# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
import json
import requests
from loguru import logger


class SendServer:
    def __init__(self, api_key: str, method: str = 'POST'):
        self.base_url = f'https://sctapi.ftqq.com/{api_key}.send'
        self.method = method

    def send_massage(self, data: dict = {}):
        title = data['title'] if 'title' in data.keys() else ''
        content = data['desp'] if 'desp' in data.keys() else ''
        send_data = {
            'title': title,
            'desp': content
        }
        try:
            resp = requests.request(method=self.method,
                                    url=self.base_url,
                                    data=send_data)

            return resp
        except Exception as e:
            logger.error(e)


class FileUtils:
    @staticmethod
    def write2json(json_path: str, data: dict):
        with open(json_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4))
        logger.info(f'write json to: {json_path}')

    @staticmethod
    def load_json(json_path: str):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        return data

    @staticmethod
    def load_md(md_path: str):
        with open(md_path, 'r', encoding='utf-8') as f:
            return f.read()
