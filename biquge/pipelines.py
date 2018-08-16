# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

rootDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')  # 根目录


class BiqugePipeline(object):
    def process_item(self, item, spider):
        '''
        :param item:
        :param spider:
        :return:
            level1 = scrapy.Field()  # 一级标签
            level2 = scrapy.Field()  # 二级标签
            author = scrapy.Field()  # 作者
            chapter = scrapy.Field()  # 三级标签,章节
            title = scrapy.Field()  # 标题
            content = scrapy.Field()  # 正文
        '''

        # 存txt
        level1 = item['level1']

        level1Dir = rootDir + '\\' + level1  # 一级目录
        # 如果不存在则创建
        if not os.path.exists(level1Dir):
            os.mkdir(level1Dir)
            level2 = item['level2']

            level2Dir = level1Dir + '\\' + level2  # 二级目录

            if not os.path.exists(level2Dir):
                os.mkdir(level2Dir)
                # 章节
                chapter = item['chapter']
                # 文件名
                filename = level2Dir + '\\' + chapter
                with open(filename + '.txt', 'w', encoding='utf-8', errors='ignore') as f:
                    # 标题。正文
                    title = item['title']
                    content = item['content']
                    f.write(str(title) + '\n' + str(content))
                    f.flush()

        return item
