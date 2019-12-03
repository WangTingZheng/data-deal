'''
@Description: 
@Author: WangTingZheng
@Date: 2019-11-22 10:48:37
@LastEditTime: 2019-11-22 11:24:14
@LastEditors: WangTingZheng
'''
from random import*
f = open("D:/File/vscode/dataDeal/AiLearning/data/10.KMeans/testSet.txt","w",encoding="utf-8")
'''
data_number=10000
while data_number!=0:
    data=[]
    data.append(int(random()*(100000-14488)+14488))
    data.append(random()*9+1)
    data.append(random()*2)
    data.append(int(random()*10))
    data_in=''
    for i in range(len(data)):
        f.write(data_in)
        data_in+=str(data[i])
        if i==len(data)-1:
            data_in+="\n"
        else:
            data_in+="\t"
    data_number-=1
    f.writelines(data_in)


'''
from baseDeal.mysql import*
table = "knn_data"
year = print_item("year",-1,table)
star = print_item("star",-1,table)
pp = print_item("star",-1,table)
time = print_item("time",-1,table)
for i in range(1000):
    tmp = str(year[i])+"\t"+str(star[i])+"\t"+str(pp[i])+"\t"+str(time[i])+"\n"
    f.write(tmp)
