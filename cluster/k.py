'''
@Description:
@Author: WangTingZheng
@Date: 2019-11-15 18:26:00
@LastEditTime: 2019-11-22 10:19:14
@LastEditors: WangTingZheng
'''
from classification.sort_list import*

class group:
    point=[]
    def add_random(self, l , c, max, min):
        import random
        for i in range(l):
            c_list=[]
            for j in range(c):
                c_list.append(random.random()*(max-min)+min)
            self.point.append(c_list)

    def return_center(self):
        point = self.point
        length = len(point[0])
        res=[]
        for i in range(length):
            tmp=0
            for j in point:
                tmp+=j[i]
            res.append(tmp/len(point))
        return res

class calcu():
    def max(self, data_list):
        return sorted(data_list)[len(data_list)-1]
    def min(self, data_list):
        return sorted(data_list)[0]
    def dis(self, data_list, point):
        res=[]
        for i in data_list:
            from classification.distance import Minkowski
            for j in point:
                dis=[]
                temp=Minkowski(i,j,2)
                dis.append(temp)
            res.append(return_min_local(dis))
        return res