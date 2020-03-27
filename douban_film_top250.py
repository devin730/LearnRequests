#!/usr/bin/python
#coding: utf-8

import requests
# from bs4 import BeautifulSoup
import time
import random
from lxml import etree
import xlwt
from MyDescription import SplitDescription

class DoubanFilmsTop250():
    def __init__(self):
        self.header = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
            'Connection': 'keep - alive'
        }
        url_start = "https://movie.douban.com/top250?start="  # .format(item)
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.worksheet = self.workbook.add_sheet('豆瓣电影Top250')

        # 设置Excel的样式
        # 设置统一的字体
        font = xlwt.Font()
        font.name = 'Time New Roman'
        font.size = 14

        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER

        self.common_style = xlwt.XFStyle()
        self.common_style.font = font

        # col 0 2 3 水平居中，其余不变
        self.style023 = xlwt.XFStyle()
        self.style023.font = font
        self.style023.alignment = alignment

        # 设置列宽
        self.worksheet.col(0).width = 256 * 6  # 256是度量单位，20表示20个字符的宽度
        self.worksheet.col(1).width = 256 * 20
        self.worksheet.col(2).width = 256 * 6
        self.worksheet.col(3).width = 256 * 8
        self.worksheet.col(4).width = 256 * 20
        self.worksheet.col(5).width = 256 * 20
        self.worksheet.col(6).width = 256 * 20
        self.worksheet.col(7).width = 256 * 20
        self.worksheet.col(8).width = 256 * 20
        self.worksheet.col(9).width = 256 * 30
        self.worksheet.col(10).width = 256 * 100

        # 设置标题栏
        self.worksheet.write(0, 0, label='排名', style=self.style023)
        self.worksheet.write(0, 1, label='电影名', style=self.common_style)
        self.worksheet.write(0, 2, label='评分', style=self.style023)
        self.worksheet.write(0, 3, label='年份', style=self.style023)
        self.worksheet.write(0, 4, label='导演', style=self.common_style)
        self.worksheet.write(0, 5, label='明星', style=self.common_style)
        self.worksheet.write(0, 6, label='国家', style=self.common_style)
        self.worksheet.write(0, 7, label='类型', style=self.common_style)
        self.worksheet.write(0, 8, label='评论数', style=self.common_style)
        self.worksheet.write(0, 9, label='短评', style=self.common_style)
        self.worksheet.write(0, 10, label='网址', style=self.common_style                  )
        

        # 爬并写入Excel
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
            title = list.xpath('div/div[2]/div[@class="hd"]/a/span[1]/text()')  # title
            film_url = list.xpath('div/div[2]/div[@class="hd"]/a/@href')  # url
            description = list.xpath('div/div[2]/div[@class="bd"]/p[1]/text()')  # description
            scores = list.xpath('div/div[2]/div[@class="bd"]/div[1]/span[2]/text()')  # scores
            comments_count = list.xpath('div/div[2]/div[@class="bd"]/div[1]/span[4]/text()')  # comments count
            quote = list.xpath('div/div[2]/div[@class="bd"]/p[2]/span/text()')  # quote
            
            x = SplitDescription(description)
            director = x.Director
            stars = x.Stars
            year = x.Year
            country = x.Country
            category = x.Category
            
            self.worksheet.write(self.film_count, 0, label=self.film_count, style=self.style023)
            self.worksheet.write(self.film_count, 1, label=title, style=self.common_style)
            self.worksheet.write(self.film_count, 2, label=scores, style=self.style023)
            self.worksheet.write(self.film_count, 3, label=year, style=self.style023)
            self.worksheet.write(self.film_count, 4, label=director, style=self.common_style)
            self.worksheet.write(self.film_count, 5, label=stars, style=self.common_style)
            self.worksheet.write(self.film_count, 6, label=country, style=self.common_style)
            self.worksheet.write(self.film_count, 7, label=category, style=self.common_style)
            self.worksheet.write(self.film_count, 8, label=comments_count, style=self.common_style)
            self.worksheet.write(self.film_count, 9, label=quote, style=self.common_style)
            self.worksheet.write(self.film_count, 10, label=film_url, style=self.common_style)
            self.film_count = self.film_count + 1

if __name__ == '__main__':
    Crawl = DoubanFilmsTop250()
