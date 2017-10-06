import sqlite3

db = 'xy.db'


#################数据库的表设计####################
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

def InitDB():
    # 连接数据库
    con = sqlite3.connect(db)
    cu = con.cursor()
    try:
        # 创建商品信息表
        cu.execute("""CREATE TABLE IF NOT EXISTS GOODSINFO(
                                                ID TEXT NOT NULL,
                                                GNAME TEXT NOT NULL,
                                                DESCRIPTION TEXT NOT NULL , 
                                                PUB_TIME TEXT NOT NULL, 
                                                PRICE REAL NOT NULL , 
                                                COMMENT_NUM INTEGER NOT NULL , 
                                                SELLER TEXT NOT NULL , 
                                                REGION TEXT NOT NULL , 
                                                VIP INTEGER NOT NULL , 
                                                LINK TEXT);""")
        # 创建卖家信息表
        cu.execute("""CREATE TABLE IF NOT EXISTS SELLERINFO(
                                                SELLER TEXT NOT NULL ,
                                                GOODS_NUM INTEGER NOT NULL ,
                                                REGION TEXT NOT NULL ,
                                                DESCRIPTION TEXT);""")
        con.commit()
    except BaseException as e:
        con.rollback()
    finally:
        cu.close()
        con.close()


def WriteIntoGoods(goods_info):
    con = sqlite3.connect(db)
    cu = con.cursor()
    try:
        for item in goods_info:
            if not cu.execute("""SELECT * FROM GOODSINFO WHERE ID = '{}';""".format(item['id'])).fetchall():
                cu.execute(
                    """INSERT INTO GOODSINFO (ID,GNAME,DESCRIPTION, PUB_TIME, PRICE, COMMENT_NUM, SELLER, REGION, VIP, LINK)
                                      VALUES ('{}','{}','{}','{}',{},{},'{}','{}',{},'{}');""".format(
                        item['id'],
                        item['name'],
                        item['description'],
                        item['time'],
                        item['price'],
                        item['comment'],
                        item['seller'],
                        item['region'],
                        item['vip'],
                        item['link']))
            con.commit()
    except BaseException as e:
        con.rollback()
    finally:
        cu.close()
        con.close()


def WriteIntoSellers(seller_info):
    con = sqlite3.connect(db)
    cu = con.cursor()
    try:
        if not cu.execute("""SELECT * FROM SELLERINFO WHERE SELLER = '{}';""".format(seller_info['seller'])).fetchall():
            cu.execute(
                """INSERT INTO SELLERINFO (SELLER,GOODS_NUM,REGION,DESCRIPTION) VALUES ('{}',{},'{}','{}');""".format(
                    seller_info['seller'], seller_info['goods_num'], seller_info['region'], seller_info['description']))
            con.commit()
    except BaseException as e:
        con.rollback()
    finally:
        cu.close()
        con.close()
