#!/usr/bin/python
#coding: utf-8


class SplitDescription():
    def __init__(self, lists):
        string1 = lists[0]
        index_director_start = string1.find('导演')
        index_director_end = string1.find('\xa0')
        index_stars_start = string1.find('主演')
        self.Director = string1[index_director_start+3:index_director_end]
        self.Stars = string1[index_stars_start+3:]
        string2 = lists[1]
        # print(string2)
        Year1, self.Country, self.Category = string2.split('/')[-3:]
        self.Year = ''
        for char in Year1:
            if char.isdigit():
                self.Year += char
        # print(self.Year)
        # self.Country = Country1.replace(' ', '')
        # self.Category = Category1.replace(' ', '')

if __name__ == "__main__":
    list = ['\n                            导演: 达伦·阿伦诺夫斯基 Darren Aronofsky\xa0\xa0\xa0主演: 艾伦·伯斯汀 Ellen Bur...',
            '\n                            2000\xa0/\xa0美国\xa0/\xa0剧情\n']
    x = SplitDescription(list)
