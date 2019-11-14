'''
@Description: distance function of KNN project
@Author: WangTingZheng
@Date: 2019-11-12 21:11:48
@LastEditTime: 2019-11-14 22:08:10
@LastEditors: WangTingZheng
'''

# old:[1,2,3]
# new:[2,3,2]
# return 1.7320508075688772
# pow_num=2: Euclidean
def Minkowski(old, new, pow_num):
    import math
    res=0
    for i  in range(len(old)):
        tmp=old[i]-new[i]
        if tmp<0:
            tmp=-tmp
        res+=math.pow(tmp,pow_num)
    return math.pow(res,1.0/pow_num)

