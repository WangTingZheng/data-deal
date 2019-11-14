import MySQLdb

account = {"host": "localhost", "username": "root", "password": "root"}


# connect and createa database
# account:  {
#           "host": "localhost",
#           "username": "root",
#           "password": "root"
# }
# return a db
def new(account):
    db = MySQLdb.connect(
        account["host"], account["username"], account["password"], "sys", charset="utf8"
    )
    return db


def create_douban(db,table):
    db = new(account)
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE if Not Exists pianyuan;")
    cursor.execute("USE pianyuan;")
    cursor.execute(
        "create table if Not Exists "+table+"(title text,type char(50),year char(50),star char(50),director text,actor text,pp char(50),time text,url char(100))ENGINE=MyISAM DEFAULT CHARSET=utf8;"
    )
    db.commit()


# insert data from dist
# db: the database which create(account) created
# info:  {
#       "title":"遗传厄运 Hereditary",
#       "year":"2018",
#       "type":"悬疑,恐怖",
#       "star":9.5,
#       "director":"阿里·艾斯特",
#       "actor":"托妮·科莱特,加布里埃尔·伯恩,亚历克斯·沃尔夫,米莉·夏普洛,安·唐德,Mallory Bechtel,Zachary Arthur,Mark Blockovich,Gabriel Monroe Eckert,John Forker,奥斯丁·R·格兰特,Rachelle Hardy,Brock McKinney,Marilyn Miller,Jason Miyagi",
#       "pp":93,
#       "time":126,
#       "film_page":"https://movie.douban.com/subject/27621727/"
# }
# return: no return
def insert_douban(db, info,table):
    cursor = db.cursor()
    cursor.execute("USE pianyuan;")
    sql = "insert into "+table+"(title,type,year,star,director,actor,pp,time,url) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(
        sql,
        (
            str(info["title"]),
            str(info["type"]),
            str(info["year"]),
            str(info["star"]),
            str(info["director"]),
            str(info["actor"]),
            str(info["pp"]),
            str(info["time"]),
            str(info["film_page"]),
        ),
    )


# search a item from database:
# db: the database which create(account) created
# item: such as "star"
# number: limit number
# number > 0 : search number data
# number <=0 : search all data
# return : return data,tmp data, deal with in print_item()
def select_douban(db, item, table,number):
    cursor = db.cursor()
    cursor.execute("USE pianyuan;")
    if number > 0:
        sql = "select " + item + " from "+table+" limit " + str(number)
    else:
        sql = "select " + item + " from "+table+";"
    res = cursor.execute(sql)
    return cursor.fetchall()


def delect(db,table):
    db = new(account)
    cursor = db.cursor()
    cursor.execute("USE pianyuan;")
    cursor.execute("drop table if Exists "+table+";")
    db.commit()


def create_pub(db):
    db = new(account)
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE if Not Exists pianyuan;")
    cursor.execute("USE pianyuan;")
    cursor.execute(
        "create table if Not Exists pub(number char(20),time char(20))ENGINE=MyISAM DEFAULT CHARSET=utf8;"
    )
    db.commit()


def insert_pub(db, info):
    cursor = db.cursor()
    cursor.execute("USE pianyuan;")
    sql = "insert into pub(number,time) values(%s,%s)"
    cursor.execute(sql, (str(info["number"]), str(info["time"])))


def get_string(string):
    res=[]
    tmp=""
    for i in string:
        try:
            int(i)
            res.append(i)
        except:
            pass
    for i in res:
        tmp+=i
    return tmp

# copy file item to mysql
# path: file path likes "./data/film.json"
def file_to_mysql(path):
    import json
    f = open(path, "r", encoding="utf-8")
    data = f.read()
    tmp = ""
    res = []
    db = new(account)
    create_douban(db,"douban")
    for i in data:
        if i == "\n":
            tmp = json.loads(tmp)
            tmp['time'] = str(tmp['time'])
            tmp['time'] = get_string(tmp['time'])
            insert_douban(db, tmp)
            tmp = ""
        else:
            tmp += i
    db.close()


# def delect_douban(db,)
# get item from mysql database
# item: like star
# number: like 2
# return ['5.1', '3.9']
def database_to_dic(number,table):
    db = new(account)
    create_douban(db,table)
    tmp = []
    res = select_douban(db, "*", table,number)
    db.close()
    for i in res:
        info={}
        info['title']=i[0]
        info['type']=i[1]
        info['year']=i[2]
        info['star']=i[3]
        info['director']=i[4]
        info['actor']=i[5]
        info['pp']=i[6]
        info['time']=i[7]
        info['url']=i[8]
        tmp.append(info)
    return tmp

def print_item(item, number,table):
    temp=database_to_dic(number,table)
    tmp=[]
    for i in temp:
        if item=="*":
            tmp.append(i)
        else:
            tmp.append(i[item])
    return tmp

# create and insert data to a table
# all: many list
# every list: {"number":1,time:"1"}
def run_pub(all):
    db = new(account)
    delect(db,"pub")
    create_pub(db)
    for i in all:
        insert_pub(db, i)
