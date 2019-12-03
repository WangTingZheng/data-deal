'''
@Description: 
@Author: WangTingZheng
@Date: 2019-11-15 18:27:38
@LastEditTime: 2019-11-15 20:28:09
@LastEditors: WangTingZheng
'''
from cluster.database import*
from baseDeal.calculation import *
from classification.sort_list import*

def ave(list_name):
    res=0
    for i in list_name:
        i=float(i)
        res+=i
    return res/len(list_name)


def return_data():
    data = get_data()
    all_data=[]
    for i in range(3):
        tmp=[]
        for a in data:
            tmp.append(float(a[i]))
        all_data.append(tmp)
    return all_data
def return_ave():
    all_data=return_data()
    res=[]
    for i in all_data:
        temp = ave(i)
        res.append(temp)
    return res

def return_max():
    data = get_data()
    res=[]
    for i in data:
        temp = return_max_local(i)
        res.append(temp)
    return res

def return_min():
    data = get_data()
    res=[]
    for i in data:
        temp = return_min_local(i)
        res.append(temp)
    return res