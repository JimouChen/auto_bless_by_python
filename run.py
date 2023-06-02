# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

from utils import SendServer, FileUtils

if __name__ == '__main__':
    cfg = FileUtils.load_json('./conf/conf.json')
    bless_data = FileUtils.load_md('./content/bless_word.md')
    server = SendServer(api_key=cfg['api_key'])
    server.send_massage({
        'title': cfg['title'],
        'desp': bless_data
    })
