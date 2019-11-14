'''
@Description:
@Author: WangTingZheng
@Date: 2019-11-08 11:21:38
@LastEditTime: 2019-11-14 23:55:40
@LastEditors: WangTingZheng
'''
from classification.database import*
test={"year":2013,"star":3.9,"people":86,"time":112}

# convert(100)

# print calculate value
# test: test data, likes test={"year":2013,"star":3.9,"people":86,"time":112}
# pow_num : the distance pow, swicth different distance
# min_num : number of standard data retrieved after sorting
# return : a float value like 6.99999999
def KNN(test,pow_num,min_num):
    data = add_dist(test,pow_num)
    res = return_calculate(test,pow_num,min_num)
    print(res)