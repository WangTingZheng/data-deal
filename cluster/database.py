'''
@Description: 
@Author: WangTingZheng
@Date: 2019-11-15 11:54:06
@LastEditTime: 2019-11-15 20:44:21
@LastEditors: WangTingZheng
'''
from baseDeal.mysql import*
account = {"host": "localhost", "username": "root", "password": "root"}
position={'year':2,'star':3,'pp':6,'time':7} #

def get_data():
    db=new(account)
    data=select_douban(db,"*","knn_data",-1)
    res=[]
    for i in data:
        tmp=[]
        tmp.append(float(i[position['year']]))
        tmp.append(float(i[position['star']]))
        tmp.append(float(i[position['pp']]))
        res.append(tmp)
    return res