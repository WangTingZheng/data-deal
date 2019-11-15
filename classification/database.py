'''
@Description: mysql operation of project KNN
@Author: WangTingZheng
@Date: 2019-11-12 21:25:02
@LastEditTime: 2019-11-15 11:25:55
@LastEditors: WangTingZheng
'''

from baseDeal.mysql import*
from classification.distance import*
from classification.sort_list import*

position={'year':2,'star':3,'pp':6,'time':7} #
account = {"host": "localhost", "username": "root", "password": "root"}

#  1. get rid of data has vaild pp value
#  2. take the first test_num.
#  3. save those data to knn_test table as test data
#  4. save rest data to knn_data table as stand data
#  test_num: the number of knn_test table
def convert(test_num):
    account = {"host": "localhost", "username": "root", "password": "root"}
    db=new(account)
    delect(db,"knn_data")
    delect(db,"knn_test")
    create_douban(db,"knn_data")
    create_douban(db,"knn_test")
    data=select_douban(db,"*","douban",-1)
    flag=0
    for i in data:
        if i[7]!="":
            info={}
            info["title"]=i[0]
            info["type"]=i[1]
            info["year"]=i[2]
            info["star"]=i[3]
            info["director"]=i[4]
            info["actor"]=i[5]
            info["pp"]=i[6]
            info["time"]=i[7]
            info["film_page"]=i[8]
            if flag>=test_num:
                insert_douban(db,info,"knn_data")
            else:
                insert_douban(db,info,"knn_test")
                flag+=1


# add dis (from test) info in stand data (table knn_data, of course in list, not in database)
# test: test data, likes test={"year":2013,"star":3.9,"people":86,"time":112}
# pow_num, the distance pow, swicth different distance
# return: ['再生勇士', '动作,犯罪', '1995', '4.7', '张建亚,李国民', '郑浩南,张志坚,吴雪雯', '106',
# '91', 'https://movie.douban.com/subject/3711787/', 34.132096331752024]
def add_dist(test, pow_num):
    db=new(account)
    data=select_douban(db,"*","knn_data",-1)
    res=[]
    flag=0
    for i in data:
        tmp = list(i)
        year = float(tmp[2])
        people = float(tmp[6])
        time = float(tmp[7])
        dist=Minkowski([year,people,time],[test['year'],test['people'],test['time']],pow_num)
        tmp.append(dist)
        res.append(tmp)
        tmp={}
    return res


# return the value of calculate
# test: test data, likes test={"year":2013,"star":3.9,"people":86,"time":112}
# pow_num : the distance pow, swicth different distance
# min_num : number of standard data retrieved after sorting
# return : a float value like 6.99999999
def return_calculate(test, pow_num, min_num):
    data = add_dist(test, pow_num)
    dis=[]
    for i in data:
        dis.append(i[len(i)-1])
    flag = min_num
    star=0
    while flag!=0:
        min = return_min_local(dis)
        star+= float(data[min][3])
        dis[min]=99999999999999999999999999
        flag-=1
    return star/min_num

def get_test(start, end, all=False):
    db=new(account)
    data=select_douban(db,"*","knn_test",-1)
    res=[]
    if all==True:
        start = 0
        end = len(data)
    for j in range(start,end):
        i = data[j]
        tmp={}
        tmp['year']=float(i[position['year']])
        tmp['star']=float(i[position['star']])
        tmp['people']=float(i[position['pp']])
        tmp['time']=float(i[position['time']])
        res.append(tmp)
    return res

#add_dist({"year":2013,"star":3.9,"people":86,"time":112},2)
