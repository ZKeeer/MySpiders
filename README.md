# XianyuSpider
爬取闲鱼0-10000价格区间内的平板信息以及卖家信息

这个爬虫使用随机选取代理IP和User-Agent</br>
代理IP抓取自各个代理IP网站的免费IP。然后验证是否可用，设置超时时间为8秒（可根据需要修改），三分钟获取一次代理IP。</br></br>

<hr />
如果想要修改这个爬虫的价格信息，或者爬取其他商品信息，在/Spider/LinkSpider.py里面修改链接和价格信息。</br>
进入“该卖家更多闲置”和“商品详情页面”时，请求头部信息需要有个参数Refer，意思是从哪个页面跳转而来，这个必须有。</br></br>

<hr />
数据库的表：</br>

平板信息表：GOODSINFO</br>
&nbsp;&nbsp;商品ID：    ID          TEXT NOT NULL</br>
&nbsp;&nbsp;商品名：    GNAME        TEXT NOT NULL</br>
&nbsp;&nbsp;描述：      DESCRIPTION TEXT NOT NULL</br>
&nbsp;&nbsp;发布时间：  PUB_TIME    TEXT NOT NULL</br>
&nbsp;&nbsp;价格：      PRICE       REAL NOT NULL</br>
&nbsp;&nbsp;留言数：    COMMENT_NUM INTEGER NOT NULL</br>
&nbsp;&nbsp;卖家：      SELLER      TEXT NOT NULL</br>
&nbsp;&nbsp;地区:       REGION      TEXT NOT NULL</br>
&nbsp;&nbsp;卖家等级：  VIP         INTEGER NOT NULL</br>
&nbsp;&nbsp;商品链接：  LINK        TEXT</br></br>
    
卖家信息表：SELLERINFO</br>
&nbsp;&nbsp;卖家昵称：    SELLER        TEXT NOT NULL</br>
&nbsp;&nbsp;闲置数量：    GOODS_NUM INTEGER NOT NULL</br>
&nbsp;&nbsp;地区：        REGION      TEXT NOT NULL</br>
&nbsp;&nbsp;所用商品描述：DESCRIPTION TEXT</br>
