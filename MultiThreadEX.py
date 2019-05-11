from threading import Thread
import requests
import random
import time
import re
import os


class MultithreadCrawler:
    def __init__(self):
        self.Links = []
        self.LinksFailed = []
        self.Pages = []
        self.Images = []
        self.UA = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12",
            "Opera/9.27 (Windows NT 5.2; U; zh-cn)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13",
            "Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 ",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 ",
            "Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; F-01D Build/F0001) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 ",
            "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; ja-jp) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7",
            "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; da-dk) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5 ",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9 ",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
        ]
        self.sleeptime = 0.1
        self.threadnums = 12
        if not os.path.exists("./MultithreadCrawlerImages"):
            os.mkdir("./MultithreadCrawlerImages")
        self.image_path = "./MultithreadCrawlerImages"

    def getLinks(self, link, minpagenum, maxpagenum):
        """
        构造需要抓取的页面链接，放在队列中供getPageContent使用
        实例page链接：http://jandan.net/pic/page-166
        link: http://jandan.net/pic/page-
        minpagenum: 1
        maxpagenum: 192
        :return:
        """
        for index in range(minpagenum, maxpagenum + 1):
            self.Links.append("{}{}".format(link, index))
        self.Links.append("#END#") #在队列中添加结束标志

    def getPageContent(self):
        """
        根据链接抓取相应页面，将结果放在Pages队列中
        :return:
        """
        head = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Connection": "keep-alive",
            "Host": "jandan.net",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
        }

        while True:

            tmp_link = self.Links.pop(0)
            # 遇到结束标志 退出线程
            if tmp_link == "#END#":
                self.Links.append("#END#")
                break
            # 这个网站没必要更换header
            # head.update({"User-Agent": random.choice(self.UA)})
            try:
                #下载网页并添加到Pages列表
                result = requests.get(tmp_link, headers=head).text
                self.Pages.append(result)
            except BaseException as e:
                self.LinksFailed.append(tmp_link)
                print("Failed Link:{}".format(tmp_link))
            #time.sleep(self.sleeptime)

        self.Pages.append("#END#")

    def getImageLink(self):
        """
        从getPageContent的抓取结果中，提取图片链接，放在队列中
        :return:
        """
        while True:
            #页面队列为空 等待0.01S
            while not self.Pages:
                time.sleep(0.01)

            content = self.Pages.pop(0)
            # 遇到结束标志  退出线程
            if content == "#END#":
                self.Pages.append("#END#")
                break
            #提取图片链接并添加到Images列表
            for item in re.findall("查看原图.+?img src=\\\"(.+?)\\\"", content):
                self.Images.append(item)
        self.Images.append("#END#") #添加结束标志

    def getImage(self):
        """
        从队列中获取一个图片抓取链接，进行抓取并保存
        :return:
        """
        while True:
            #队列为空等待0.01S
            while not self.Images:
                time.sleep(0.01)

            url = self.Images.pop(0)
            #遇到END标志，推出线程
            if url == "#END#":
                self.Images.append("#END#")
                break
            try:
                #构造参数
                img_name = self.image_path + "/" + url.split("/")[-1]
                img_host = url.split("/")[2]
                img_url = "http:" + url
                head = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Connection": "keep-alive",
                    "Host": img_host,
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
                }
                #下载图片
                content = requests.get(url=img_url, headers=head).content
                #保存到指定位置
                with open(img_name, "wb") as fw:
                    fw.write(content)
            except BaseException as e:
                print("failed img link: ", url)
                continue

    def main(self):
        """
        组织抓取过程
        :return:
        """
        t_list = []
        self.getLinks("http://jandan.net/pic/page-", 1, 192) #构造链接
        for index in range(0, self.threadnums):     #获取页面线程
            t_list.append(Thread(target=self.getPageContent))
        for index in range(0, self.threadnums):     #提取图片链接线程
            t_list.append(Thread(target=self.getImageLink))
        for index in range(0, self.threadnums * 2):  #获取图片线程
            t_list.append(Thread(target=self.getImage))

        for t in t_list: #启动线程
            t.start()
        for t in t_list: #等待结束
            t.join()


if __name__ == '__main__':
    st = time.time()
    solution = MultithreadCrawler()
    solution.main()
    print(time.time()-st)
