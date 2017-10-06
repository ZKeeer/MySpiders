import os
import random
import re
import traceback

import requests

from JandanSpider.Util import Config

primary_level = "./DownLoad/"
second_level = "./DownLoad/Image/"


def page_downloader(tar_url, host=None):
    url_content = ""
    try:
        url_content = requests.get(tar_url,
                                   headers={
                                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                       'Accept-Encoding': 'gzip, deflate, compress',
                                       'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ru;q=0.4',
                                       'Cache-Control': 'no-cache',
                                       'Connection': 'keep-alive',
                                       'Upgrade-Insecure-Requests': "1",
                                       'User-Agent': random.choice(Config.UserAgents)
                                   }).text
    except BaseException as e:
        pass
    finally:
        return url_content


def image_downloader(image_url, Refer=None, image_name=None):
    if not image_name:
        if not os.path.exists(primary_level):
            os.mkdir(primary_level)
        if not os.path.exists(second_level):
            os.mkdir(second_level)
        try:
            image_name = re.findall("([\w]+?\.(?:jpeg|jpg|png|bmp|gif))", image_url)[0]
            image_name = second_level + image_name
        except BaseException as e:
            print("获取文件名失败 url:{}".format(image_url))

    #referer
    "http://jandan.net/ooxx/page-12#comments"
    num = re.findall("http://jandan.net/ooxx/page-([\d]+?)#comments",Refer)[0]
    referer = "http://jandan.net/ooxx/page-{}".format(num)

    #获取
    try:
        url_content = requests.get(image_url,
                                   timeout=30,
                                   headers={
                                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                       'Accept-Encoding': 'gzip, deflate, compress',
                                       'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ru;q=0.4',
                                       'Cache-Control': 'no-cache',
                                       'Connection': 'keep-alive',
                                       'Referer':referer,
                                       'Upgrade-Insecure-Requests': "1",
                                       'User-Agent': random.choice(Config.UserAgents)
                                   }).content

        with open(image_name, "wb") as fw:
            fw.write(url_content)
    except BaseException as e:
        traceback.print_exc()
        #print("图片获取失败：{}".format(image_name))
