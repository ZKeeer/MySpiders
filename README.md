# XianyuSpider
爬取闲鱼0-10000价格区间内的平板信息以及卖家信息

如果想要修改这个爬虫的价格信息，或者爬取其他商品信息，在/Spider/LinkSpider.py里面修改链接和价格信息。</br>
数据库的表：</br>
 平板信息表：GOODSINFO</br>
    商品ID：    ID          TEXT NOT NULL</br>
    商品名：    GNAME        TEXT NOT NULL</br>
    描述：      DESCRIPTION TEXT NOT NULL</br>
    发布时间：  PUB_TIME    TEXT NOT NULL</br>
    价格：      PRICE       REAL NOT NULL</br>
    留言数：    COMMENT_NUM INTEGER NOT NULL</br>
    卖家：      SELLER      TEXT NOT NULL</br>
    地区:       REGION      TEXT NOT NULL</br>
    卖家等级：  VIP         INTEGER NOT NULL</br>
    商品链接：  LINK        TEXT</br></br>
    
 卖家信息表：SELLERINFO</br>
    卖家昵称：    SELLER        TEXT NOT NULL</br>
    闲置数量：    GOODS_NUM INTEGER NOT NULL</br>
    地区：        REGION      TEXT NOT NULL</br>
    所用商品描述：DESCRIPTION TEXT</br>
