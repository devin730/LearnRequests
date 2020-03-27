#!/usr/bin/python
#coding: utf-8

import requests
from bs4 import BeautifulSoup
import time
import random

# 设置header
header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Connection': 'keep - alive'
}
movie_list = []


def get_pages_link():
    # https://movie.douban.com/top250?start=25
    for item in range(0, 250, 25):
        url = "https://movie.douban.com/top250?start={}".format(item)
        web_data = requests.get(url, headers=header)
        time.sleep(0.5 + random.random())
        soup = BeautifulSoup(web_data.text, 'lxml')
        for movie in soup.select('#wrapper li'):
            href = movie.select('.hd > a')[0]['href']
            name = movie.select('.hd > a > span')[0].text
            star = movie.select('.rating_num')[0].text
            people = movie.select('.star > span')[3].text
            try:
                quote = movie.select('.inq')[0].text
            except:
                print("没有quote哦")
                quote = None
            data = {
                'url': href,
                '评价人数': people,
                '片名': name,
                '评分': star,
                '名言': quote
            }
            print(data)
        print('\n' + ' - ' * 50 + '\n')


if __name__ == '__main__':
    get_pages_link()