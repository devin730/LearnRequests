#!/usr/bin/python
#coding: utf-8

import requests
# from bs4 import BeautifulSoup
import time
import random
from lxml import etree
import xlwt
from MyDescription import SplitDescription

class DoubanFilesTop250():
    def __init__(self):
        self.header = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
            'Connection': 'keep - alive'
        }
        url_start = "https://movie.douban.com/top250?start="  # .format(item)
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.worksheet = self.workbook.add_sheet('豆瓣电影Top250')
        self.worksheet.write(0, 0, label='排名')
        self.worksheet.write(0, 1, label='电影名')
        self.worksheet.write(0, 2, label='评分')
        self.worksheet.write(0, 3, label='年份')
        self.worksheet.write(0, 4, label='导演')
        self.worksheet.write(0, 5, label='明星')
        self.worksheet.write(0, 6, label='国家')
        self.worksheet.write(0, 7, label='类型')
        self.worksheet.write(0, 8, label='评论数')
        self.worksheet.write(0, 9, label='短评')
        self.worksheet.write(0, 10, label='网址')
        self.film_count = 1
        for page in range(0, 250, 25):
            url = url_start + str(page)
            self.crawl(url)
            sleep_time = 1 + random.random()
            time.sleep(sleep_time)
        self.workbook.save('./豆瓣电影TOP250.xls')

    def crawl(self, url):
        print('crawl page....')
        web_data = requests.get(url, headers=self.header).text
        selector = etree.HTML(web_data)
        li_lists = selector.xpath('//ol[@class="grid_view"]/li')
        # print(li_lists)
        for list in li_lists:
            # print(list.xpath('//div[@class="hd"]/a/span[1]/text()'))
            # print('_____________________________________________________')
            # print(list.xpath('div/div[2]/div[@class="hd"]/a/span[1]/text()'))  # title
            # print(list.xpath('div/div[2]/div[@class="hd"]/a/@href'))  # url
            # print(list.xpath('div/div[2]/div[@class="bd"]/p[1]/text()'))  #! description 后期可以处理一下这个文本
            # print(list.xpath('div/div[2]/div[@class="bd"]/div[1]/span[2]/text()'))  # scores
            # print(list.xpath('div/div[2]/div[@class="bd"]/div[1]/span[4]/text()'))  # comments count
            # print(list.xpath('div/div[2]/div[@class="bd"]/p[2]/span/text()'))  # quote

            title = list.xpath('div/div[2]/div[@class="hd"]/a/span[1]/text()')  # title
            film_url = list.xpath('div/div[2]/div[@class="hd"]/a/@href')  # url
            description = list.xpath('div/div[2]/div[@class="bd"]/p[1]/text()')  #! description 后期可以处理一下这个文本
            scores = list.xpath('div/div[2]/div[@class="bd"]/div[1]/span[2]/text()')  # scores
            comments_count = list.xpath('div/div[2]/div[@class="bd"]/div[1]/span[4]/text()')  # comments count
            quote = list.xpath('div/div[2]/div[@class="bd"]/p[2]/span/text()')  # quote
            
            x = SplitDescription(description)
            director = x.Director
            stars = x.Stars
            year = x.Year
            country = x.Country
            category = x.Category
            
            self.worksheet.write(self.film_count, 0, label=self.film_count)
            self.worksheet.write(self.film_count, 1, label=title)
            self.worksheet.write(self.film_count, 2, label=scores)
            self.worksheet.write(self.film_count, 3, label=year)
            self.worksheet.write(self.film_count, 4, label=director)
            self.worksheet.write(self.film_count, 5, label=stars)
            self.worksheet.write(self.film_count, 6, label=country)
            self.worksheet.write(self.film_count, 7, label=category)
            self.worksheet.write(self.film_count, 8, label=comments_count)
            self.worksheet.write(self.film_count, 9, label=quote)
            self.worksheet.write(self.film_count, 10, label=film_url)
            self.film_count = self.film_count + 1

if __name__ == '__main__':
    Crawl = DoubanFilesTop250()
