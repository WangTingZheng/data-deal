'''
@Description: finally operation of KNN project
@Author: WangTingZheng
@Date: 2019-11-08 11:21:38
@LastEditTime: 2019-11-15 11:45:03
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
    return res



def KNN_all(test_range,pow_num, min_num):
    f = open("./classification/data/data.py","w",encoding="utf-8")
    f.write("{")
    if test_range!="all" and len(test_range)>=2 and type(test_range) is list:
        res = get_test(test_range[0],test_range[1]+1,False)
    elif test_range=="all":
        res = get_test(1,1,True)
    else:
        print("test_range value error!")
        exit()
    for i in range(len(res)):
        res_data=KNN(res[i], pow_num,min_num)
        res[i]['calculate']=res_data
        if i==len(res)-1:
            f.write(str(res[i])+"}")
        else:
            f.write(str(res[i])+",")
    f.close()