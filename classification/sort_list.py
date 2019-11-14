'''
@Description: sort operation of KNN project
@Author: WangTingZheng
@Date: 2019-11-12 22:02:58
@LastEditTime: 2019-11-14 21:05:32
@LastEditors: WangTingZheng
'''

# list_test : a test list val:[32,3,1,40,28,22]
# return: 2
bigger_than_any=9999999999999999

def return_min_local(list_test):
    min=0
    now=1
    while now<=len(list_test)-1:
        if list_test[min]>=list_test[now]:
            min=now
        now+=1
    return min

def return_max_local(list_test):
    max=0
    now=1
    while now<=len(list_test)-1:
        if list_test[max]<=list_test[now]:
            max=now
        now+=1
    return max


def return_sort(list_test):
    i=0
    temp=[]
    while i < len(list_test):
        res = return_min_local(list_test)
        list_test[res]=bigger_than_any
        temp.append(res)
        i+=1
    return temp
#print(return_sort([32,3,1,40,28,22]))
