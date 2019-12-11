from lxml import etree

import requests as rq

CNYES_URL = "https://news.cnyes.com/news/cat/headline?exp=a"


class News():

    def __init__(self):
        pass

    def cnyes(self, count):
        page = rq.get(CNYES_URL)
        tree = etree.HTML(page.text)
        path = ".//a[@class=\"_1Zdp\"]/@href"
        list = tree.xpath(path)[:count]
        urls = ["https://news.cnyes.com/" + x for x in list]
        return urls
