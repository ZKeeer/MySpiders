import os
from os.path import exists
from random import choice
from threading import Thread
from time import sleep

from DataBase.OperateDB import InitDB
from Spider import GoodsSpider, ListSpider
from Spider.GetIPProxy import getips

from XianyuSpider.Spider import SellerSpider


# https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.609c25ca0hst7I&catid=50100424&st_trust=1&start=0&end=50&page=4&ist=0
# 价格区间：0-10000  步长：10

def GetPageInfo(url_tar):
    seller_url_list = GoodsSpider.GetGoodsInfo(url_tar)
    thread_list = []
    for item in seller_url_list:
        thread_list.append(Thread(target=SellerSpider.GetSellerInfo, args=(url_tar, item)))
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()


def GetData():
    url_list = ListSpider.GetLinkList()
    for page_url_item in url_list:
        try:
            GetPageInfo(page_url_item)
        except BaseException as e:
            pass

        # 随机睡眠，睡眠时间：0.5-1.5
        sleep_time = float(choice(range(5, 16))) / 10
        sleep(sleep_time)
    with open("completed.txt", "w")as fw:
        fw.write("")


def GetIP():
    while not exists("./completed.txt"):
        getips()
        sleep(120) #三分钟取一次IP


if __name__ == '__main__':

    InitDB()
    if os.path.exists("completed.txt"):
        os.rename("completed.txt")
    GetIP()

    ip_thread = Thread(target=GetIP)
    data_thread = Thread(target=GetData)

    data_thread.start()
    ip_thread.start()

    data_thread.join()
    ip_thread.join()
