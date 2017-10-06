import random
import re
import time
import traceback

import requests

from XianyuSpider.DataBase import OperateDB
from .GetIPProxy import GetIpToUse


def GetPageContent(url_seed):
    """
    获取页面内容
    :param url_seed:网页链接
    :return:链接页面上的内容
    """
    # 随机获取用户代理
    user_agents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko/20070215 Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13",
        "Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 ",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 ",
        "Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; F-01D Build/F0001) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 ",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; ja-jp) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; da-dk) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5 ",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9 ",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
    ]
    user_agent = random.choice(user_agents)

    # 构造请求
    try:
        req = requests.get(
            url=url_seed,
            proxies=GetIpToUse(),
            headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': user_agent
            })
    except BaseException as e:
        with open('log.txt', 'a') as fa:
            fa.write("Time: {}{}".format(time.ctime(), '\n'))
        traceback.print_exc(file=open('log.txt', 'a'))
        with open('log.txt', 'a') as fa:
            fa.write('\n\n')
        return ''

    print("Time:{} status:{}".format(time.ctime(), req.status_code))
    return req.text


def GetGoodsInfo(url_curr):
    """
    解析提取页面内容，写入数据库
    :param url_curr:网页的html内容
    :return:该页面上卖家的“更多闲置”链接
    """
    goods_info = []
    url_content = GetPageContent(url_curr)
    lt = time.localtime()
    # 获取提取页面的时间
    current_time = lt.tm_year.__str__() \
                   + lt.tm_mon.__str__() \
                   + lt.tm_mday.__str__() \
                   + "-" \
                   + lt.tm_hour.__str__() \
                   + lt.tm_min.__str__() \
                   + lt.tm_sec.__str__()

    if re.findall(r"亲.你太潮了.闲鱼.淘宝二手里暂时还找不到你搜索的东西呢", url_content):
        print("This page is empty. {}".format(url_curr))
        return []

    # 1.获取页面上商品名
    names = re.findall(r"<h4 class=\"item-title\"><a target=\"_blank\" href=\"(.*)\">(.*)</a>", url_content)
    # 2.获取简短的商品描述
    descriptions = re.findall(r"<div class=\"item-description\">(.*)</div>", url_content)
    # 3.获取页面上发布时间，如果是几小时/分钟/天前，转换成标准的2017/08/04  对应年月日
    times = re.findall(r"<span class=\"item-pub-time\">(.*?)</span>", url_content)
    # 4.获取页面上商品价格
    prices = re.findall(r"<span class=\"price\"><b>&yen</b><em>([\d\.]*)</em>", url_content)
    # 5.获取商品留言数
    comments = re.findall(r"留言<em class=\"number\">(\d*)</em>", url_content)
    # 6.获取页面上卖家名字
    sellers = re.findall(r"data-nick=\"(.*?)\"", url_content)
    # 7.获取页面上卖家地区
    regions = re.findall(r"<div class=\"seller-location\">(.*?)</div>", url_content)
    # 8.获取页面上卖家等级
    vips = re.findall(r"<span class=\"sh-user-vip .*\">vip(\d*)</span>", url_content)
    # 9.获取卖家闲置物品链接
    things_link = re.findall(r"<a href=\"(.*)\" class=\"number\" target=\"_blank\">该卖家更多闲置</a>", url_content)
    # 10.获取商品ID
    ids = re.findall(r"<a target=\"_blank\" href=\"//2\.taobao\.com/item\.htm\?id=(.*)\"><img", url_content)

    # 标准化时间2017/08/21
    t_time = []
    for item in times:
        if "分钟" in item or "小时" in item:
            year = str(time.localtime().tm_year)
            mon = str(time.localtime().tm_mon)
            if mon.__len__() == 1:
                mon = "0{}".format(mon)
            day = str(time.localtime().tm_mday)
            if day.__len__() == 1:
                day = "0{}".format(day)
            t_time.append("{}/{}/{}".format(year, mon, day))
        elif "天" in item:
            gap_day = int(re.findall(r"(\d*)天前", item)[0])
            year = str(time.localtime().tm_year)
            mon = str(time.localtime().tm_mon)
            if mon.__len__() == 1:
                mon = "0{}".format(mon)
            day = time.localtime().tm_mday
            day = str(day - gap_day)
            if day.__len__() == 1:
                day = "0{}".format(day)
            t_time.append("{}/{}/{}".format(year, mon, day))
        else:
            t_time.append(item.replace(".", "/"))
    times = t_time

    # 分离商品名称和链接，给商品连接加上https:
    goods_link = []
    goods_name = []
    for item in names:
        goods_link.append("https:{}".format(item[0]))
        goods_name.append(item[1])

    # 给更多闲置的IP地址加上https:
    t_things_link = []
    for item in things_link:
        t_things_link.append("https:{}".format(item))
    things_link = t_things_link

    # 构造字典列表并返回
    for n, l, d, t, p, c, s, r, v, gid in zip(goods_name, goods_link, descriptions, times, prices, comments, sellers,
                                              regions, vips,
                                              ids):
        goods_info.append(
            {"name": n, "description": d, "time": t, "price": float(p), "comment": int(c), "seller": s, "region": r,
             "vip": int(v), "current_time": current_time, "link": l, "id": gid})

    OperateDB.WriteIntoGoods(goods_info)

    return things_link
