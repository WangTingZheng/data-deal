'''
@Description: main file to test
@Author: WangTingZheng
@Date: 2019-11-14 19:37:16
@LastEditTime: 2019-11-22 10:39:05
@LastEditors: WangTingZheng
'''
from cluster.k import*
g = group()
c= calcu()

def return_max_min(all_data):
    res=[]
    for j in range(len(all_data[0])):
        temp=[]
        for i in all_data:
            temp.append(i[j])
        res.append(temp)
    max=[]
    min=[]
    for x in res:
        max.append(c.max(x))
        min.append(c.min(x))
    return max,min

def main(all_data):
    def return_belong(all_data, k):
        max=return_max_min(all_data)[0]
        min = return_max_min(all_data)[1]
        g.add_random(k,3,return_max_min(all_data)[0],max,min)
        bein_list=[]
        for i in all_data:
            res=[]
            bein=-1
            for j in range(k):
                dis = c.dis(i,g.point[j])
                res.append(dis)
            min_va=c.min(res)
            for m in range(len(res)):
                if res[m]==min_va:
                    bein=m
            bein_list.append(bein)