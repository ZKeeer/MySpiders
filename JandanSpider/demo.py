from threading import Thread

from JandanSpider.Util import PageParser, Downloader, Record

# 初始化各种变量
page_list = []
max_page = 0
RegEx_img = "<a href=\"([\w\/\.]+?)\" target"
RegEx_max_page = "\"current-comment-page\">[(\d*?)]</span>"

#获取访问过的页面列表
rec_dict = Record.Read()
page_viewed = rec_dict.get("viewed", [])

#获取最新的页面值
content = Downloader.page_downloader("http://jandan.net/ooxx")
max_page = PageParser.parser(content, RegEx=RegEx_max_page)[0]
print("解析结果：{}".format(PageParser.parser(content, RegEx=RegEx_max_page)))

#构造页面地址
for index in range(max_page, 0, -1):
    page_list.append("http://jandan.net/ooxx/page-{}#comments".format(index))

#遍历页面
for page_item in page_list:
    #如果页面已经访问过，continue
    #如果没有，添加到viewed列表，然后进行访问
    if page_item in page_viewed:
        continue
    else:
        page_viewed.append(page_item)

    # 输出当前访问的页面url
    print("page: {}".format(page_item))
    threads_list = []
    content = Downloader.page_downloader(tar_url=page_item) #下载页面
    img_list = PageParser.parser(content, RegEx=RegEx_img) #解析页面，获取图片链接
    #每张图片建立一个线程去下载
    for img_item in img_list:
        threads_list.append(Thread(target=Downloader.image_downloader, args=["http:{}".format(img_item), page_item]))
    for t in threads_list:
        t.start()
    for t in threads_list:
        t.join()

#把最新的页面，最新的页数，访问过的页面记录
Record.Write({"page_num": index, "page_url": page_item, "viewed": page_viewed})
