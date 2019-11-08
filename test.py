from app.calculation import *
from app.mysql import *
def main():
    star_data = print_item("star", -1)
    res = []
    for i in star_data:
        res.append(float(i))

    year_data = print_item("year", -1)
    year = []
    for i in year_data:
        year.append(int(i))
    single_normal_va=single_normal()
    print("平均数:"+str(single_normal.ave(single_normal_va,res)))
    print("中位数:"+str(single_normal.med(single_normal_va,res)))
    print("中列数:"+str(single_normal.median(single_normal_va,res)))
    print("四分位数及四分位极:"+str(single_normal.qua(single_normal_va,res)))
    single_advacne_va=single_advacne()
    print("加权平均数:"+str(single_advacne.dave(single_advacne_va,res)))
    print("熵:"+str(single_advacne.entropy(single_advacne_va,res)))
    print("方差:"+str(single_advacne.fc(single_normal_va,res)))
    print("极差:"+str(single_advacne.jc(single_normal_va,res)))
    print("绝对平均偏差:"+str(single_advacne.jdfc(single_normal_va,res)))
    print("截断均值:"+str(single_advacne.juz(single_normal_va,res)))
    print("中位数绝对偏差:"+str(single_advacne.mad(single_normal_va,res)))
    mixed_va=mixed()
    print("线性相关系数"+str(mixed.lcc(mixed_va,res,year)))
    print("余弦相似度"+str(mixed.cosl(mixed_va,res,year)))
    distance_va=distance()
    coefficient_va=coefficient()
    print("符号属性变量:"+str(coefficient.fuhao(coefficient_va,res,year)))
    print("顺序变量:"+str(coefficient.sunxu(coefficient_va,res)))

main()