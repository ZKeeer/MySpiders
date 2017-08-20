import sqlite3

con = sqlite3.connect('xy.db')
cu = con.cursor()
# 平板信息表：goodsinfo
#    商品ID：    ID          TEXT NOT NULL
#    商品名：    GNAME        TEXT NOT NULL
#    描述：      DESCRIPTION TEXT NOT NULL
#    发布时间：  PUB_TIME    TEXT NOT NULL
#    价格：      PRICE       REAL NOT NULL
#    留言数：    COMMENT_NUM INTEGER NOT NULL
#    卖家：      SELLER      TEXT NOT NULL
#    地区:       REGION      TEXT NOT NULL
#    卖家等级：  VIP         INTEGER NOT NULL
#    商品链接：  LINK        TEXT
#
# 卖家信息表：sellerinfo
#    卖家昵称：    SELLER        TEXT NOT NULL
#    闲置数量：    GOODS_NUM INTEGER NOT NULL
#    地区：        REGION      TEXT NOT NULL
#    所用商品描述：DESCRIPTION TEXT

count_dict = {}

try:
    count = 0
    for item in cu.execute("""SELECT REGION FROM GOODSINFO;""").fetchall():
        if item:
            count_dict.update({item[0]: count_dict.get(item[0], 0) + 1})
            print(item[0], item)
        else:
            count += 1
            print("{}: this item is none.".format(count))
except BaseException as e:
    pass
finally:
    cu.close()
    con.close()
    for k, v in zip(count_dict.keys(), count_dict.values()):
        if "广东" in k:
            print(k, v)