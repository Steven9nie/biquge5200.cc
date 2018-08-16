# -*- coding: utf-8 -*-

import scrapy
from biquge.items import BiqugeItem


class MybiqugeSpider(scrapy.Spider):

    name = 'biquge'
    allowed_domains = ['biquge5200.cc']
    start_urls = ['http://biquge5200.cc']

    def parse(self, response):
        # 抓取一级标签
        level1List = response.xpath('//div[@class=\'nav\']/ul/li[position()>2]')
        for i in level1List:
            level1Url = "http://" + i.xpath("./a/@href")[0].extract()[2:]
            level1 = i.xpath("./a/text()")[0].extract()

            # 构建一个请求
            request = scrapy.Request(level1Url, callback=self.get_level2)
            request.meta['level1'] = level1
            print(level1, level1Url)
            yield request

    def get_level2(self, response):
        '''
        抓取二级标签
        :param response:
        :return:
        '''
        # 二级
        level2List = response.xpath("//div[@class='r']//li")

        for i in level2List:
            level2 = i.xpath("./span/a/text()")[0].extract()
            level2Url = i.xpath("./span/a/@href")[0].extract()
            author = i.xpath("./span[2]/text()")[0].extract()

            print('====', level2, level2Url, author)

            # 构建请求
            request = scrapy.Request(level2Url, callback=self.get_chapter)
            # .meta[]只能传一级
            request.meta['level1'] = response.meta['level1']
            request.meta['level2'] = level2
            request.meta['author'] = author

            yield request

    def get_chapter(self, response):
        '''
        获取章节
        :param response:
        :return:
        '''

        level3List = response.xpath("//div[@id='list']//dd[position()>9]")
        for i in level3List:
            chapter = i.xpath("./a/text()")[0].extract()
            chapterUrl = i.xpath("./a/@href")[0].extract()
            # print("==========", chapter, chapterUrl)

            request = scrapy.Request(chapterUrl, callback=self.get_content)
            request.meta['level1'] = response.meta['level1']
            request.meta['level2'] = response.meta['level2']
            request.meta['author'] = response.meta['author']
            request.meta['chapter'] = chapter

            yield request

    def get_content(self, response):
        '''
        抓取小说正文
        :param response:
        :return:
        '''

        title = response.xpath("//div[@class=\"bookname\"]/h1/text()")[0].extract()

        contentList = response.xpath("//div[@id=\"content\"]//text()")
        print(title)

        content = ""
        for i in contentList:
            content += i.extract().replace("\u3000", '').replace('\r\n', '').replace('\t', '') + '\n'

        item = BiqugeItem()

        item["level1"] = response.meta['level1']  # 一级标签
        item["level2"] = response.meta['level2']  # 二级标签
        item['author'] = response.meta['author']  # 作者
        item["chapter"] = response.meta['chapter']  # 三级标签,章节

        item["title"] = title  # 标题
        item["content"] = content  # 正文

        yield item
