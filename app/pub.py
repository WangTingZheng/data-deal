from app.mysql import *
from app.apart import *

a = [1, 2, 2, 2, 3, 4, 4, 5, 7]

# deal counter string
# arry: data list likes: [1,2,2,2,3,4,4,5,7]
# return :a list of number:time  2: 3, 4: 2, 1: 1, 3: 1, 5: 1, 7: 1,
def get_count(arry):
    from collections import Counter

    coun = Counter(arry)
    coun = str(coun)
    coun = coun.replace("Counter({", "").replace("})", "")
    coun += ","
    return coun


# get number from count reslut
# arry: count reslut likes ['2:3', '4:2', '1:1', '3:1', '5:1', '7:1']
# return: ['2', '4', '1', '3', '5', '7']
def get_number(arry):
    number = []
    for m in arry:
        m += ":"
        num2 = apart(m, ":")
        number.append(num2[0])
    return number


# get time from count reslut
# arry: count reslut likes ['2:3', '4:2', '1:1', '3:1', '5:1', '7:1']
# return : ['3', '2', '1', '1', '1', '1']
def get_time(arry):
    time = []
    for j in arry:
        j += ":"
        num1 = apart(j, ":")
        time.append(num1[1])
    return time


# switch string count result
# res : count reslut likes ['2:3', '4:2', '1:1', '3:1', '5:1', '7:1']
# return: ['3:2', '2:4', '1:1', '1:3', '1:5', '1:7']
def switch(res):
    number = get_number(res)
    time = get_time(res)
    tmp = []
    for n in range(len(number)):
        temp = time[n] + ":" + number[n]
        tmp.append(temp)
    return tmp


# change string postion in  count result
# arry:  count reslut likes ['2:3', '4:2', '1:1', '3:1', '5:1', '7:1']
# return:['7:1', '5:1', '3:1', '1:1', '4:2', '2:3']
def change(arry):
    res = []
    for i in range(len(arry)):
        j = len(arry) - i - 1
        res.append(arry[j])
    return res


# sort num
# arry: data list likes: [1,2,2,2,3,4,4,5,7]
# return [
#           {
#               'number': 2, 'time': 3
#           },
#           {
#               'number': 4, 'time': 2
#           },
#           {
#               'number': 7, 'time': 1
#           },
#           {
#               'number': 5, 'time': 1
#           },
#           {
#               'number': 3, 'time': 1
#           },
#           {
#               'number': 1, 'time': 1
#           }
# ]
def sorted_num(arry):
    coun = get_count(arry)
    res = apart(coun, ",")
    number = get_number(res)
    time = get_time(res)
    tmp = switch(res)
    all = []
    info = {}
    for i in tmp:
        i += ":"
        temp = apart(i, ":")
        info["number"] = temp[1]
        info["time"] = temp[0]
        all.append(info)
        info = {}
    return all
