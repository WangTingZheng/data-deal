# 均值 中位数  众数 中列数 四位分数


class single_normal:
    # 计算均值
    # num: [1,2,3,4,5,6,7,8,9,10]
    # return: 5.5
    def ave(self, num):
        nsum = 0
        for i in range(len(num)):
            nsum += num[i]
        return nsum / len(num)

    # 中位数
    def med(self, num):
        listnum = [num[i] for i in range(len(num))]
        listnum.sort()
        lnum = len(num)
        if lnum % 2 == 1:
            i = int((lnum + 1) / 2) - 1
            return listnum[i]
        else:
            i = int(lnum / 2) - 1
            return (listnum[i] + listnum[i + 1]) / 2

    # 众数
    def pub(self, num, d=0):
        dictnum = {}
        for i in range(len(num)):
            if num[i] in dictnum.keys():
                dictnum[num[i]] += 1
            else:
                dictnum.setdefault(num[i], 1)
        maxnum = 0
        maxkey = 0
        for k, v in dictnum.items():
            if v > maxnum:
                maxnum = v
                maxkey = k
        return maxkey

    # 返回众数的位置
    def pub_post(self, num, d=0):
        pub_res = pub(self, num, d)
        res = []
        for i in num:
            if i == pub_res:
                res.append(i)
        return res

    # 中列数
    def median(self, num):
        max = 0
        min = 3000
        for i in num:
            if i > max:
                max = i
            if i < min:
                min = i
        return (max + min) / 2

    # 四分位数及四分位极
    def qua(self, num):
        res = []
        num.sort()
        l = num[0 : int(len(num) / 2)]
        c = num[int(len(num) / 2) :]
        return self.med(l), self.med(c), self.med(c) - self.med(l)


import math

# 加权算术均值 截断均值 极差  方差 绝对平均偏差 中位数绝对偏差 熵
class single_advacne:
    # 加权平均数
    def dave(self, num):
        avg = 0
        for c in num:
            if c <= 2.5:
                c = 3 * c
            elif c <= 5.0:
                c = 2 * c
            elif c >= 7.5:
                c = c / 2
            avg = avg + c
        return avg / len(num)

    # 截断均值
    def juz(self, num, d=10):
        l = num[int(len(num) * (d / 100)) : len(num) - int(len(num) * (d / 100))]
        return self.ave(l)

    # 极差
    def jc(self, num):
        max = 0
        min = 3000
        for i in num:
            if i > max:
                max = i
            if i < min:
                min = i
        return max - min

    # 方差
    def fc(self, num):
        avg = self.ave(num)
        d = 0
        for c in num:
            d = d + (c - avg) ** 2
        return d / (len(num) - 1)

    # 绝对平均偏差
    def jdfc(self, num):
        l = []
        j = 0
        k = 0
        ave = self.ave(num)
        for c in num:
            l.append(abs(c - ave))
            j = j + abs(c - ave)
            k = k + 1
        return j / k

    # 中位数绝对偏差
    def mad(self, num):
        l = []
        meds = self.med(num)
        for c in num:
            l.append(abs(c - meds))
        return self.med(l)

    # 计算熵
    def entropy(self, num):
        result = -1
        if len(num) > 0:
            result = 0
        for x in num:
            result += -1 * (x) * math.log(x, 2)
        return result


# 线性相关系
# 数 余弦相似度  离散相似度 欧几里得距离 Canberra距离
# Bray Curtis距离 Czekanowski距离


class mixed:
    # 线性相关系数
    def lcc(self, numX, numY):
        lens = len(numX)
        single = single_normal()
        ave_x = single_normal.ave(single, numX)
        ave_y = single_normal.ave(single, numY)

        def x(numX, numY):
            res = 0
            for i in range(lens):
                res += (numX[i] - ave_x) * (numY[i] - ave_y)
            return res

        def y(numX, numY):
            res = 0
            one = 0
            two = 0
            for i in range(lens):
                one += (numX[i] - ave_x) * (numX[i] - ave_x)
                two += (numY[i] - ave_y) * (numY[i] - ave_y)
            res = math.sqrt(one) * math.sqrt(two)
            return res

        return x(numX, numY) / y(numX, numY)

    # 余弦相似度
    def cosl(self, numX, numY):
        def ve(numX, numY):
            res = 0
            for i in range(len(numX)):
                res += numX[i] * numY[i]
            return res

        def lenX(numX):
            res = 0
            for i in numX:
                res += i * i
            return math.sqrt(res)

        def lenY(numY):
            res = 0
            for i in numY:
                res += i * i
            return math.sqrt(res)

        return ve(numX, numY) / (lenX(numX) * lenY(numY))

    # 离散相似度
    def ds(self, numX, numY):
        print("没做")


class distance:
    # 闵可夫斯基
    # flag = 1: 城市块（曼哈顿距离）
    # flag = 2: 欧几里得距离
    def Minkowski(self, P0, P1, flag):
        def absolute(x):
            if x < 0:
                return -1 * x
            return x

        def MinkowskiO(x1, y1, x2, y2, flag):
            x = pow((x1 - x2), flag)
            x = absolute(x)
            y = pow((y1 - y2), flag)
            y = absolute(y)
            res = x + y
            res = pow(res, 1 / flag)
            return res

        return MinkowskiO(P0[0], P0[1], P1[0], P1[1], flag)

    # 切比雪夫距离
    def Chebyshev(self, P0, P1):
        def absolute(x):
            if x < 0:
                return -1 * x
            return x

        def max(x, y):
            if x > y:
                return x
            else:
                return y

        return max(absolute(P0[0] - P1[0]), absolute(P0[1] - P1[1]))

    # 马氏距离
    # x = [3, 5, 2, 8]
    # y = [4, 6, 2, 4]
    # return [1.243163121016122, 1.2431631210161223,
    #        2.1320071635561044, 2.4494897427831783,
    #        2.2763607319179844, 2.2763607319179844]
    def Mahalanobis(self, x, y):
        import numpy as np

        X = np.vstack([x, y])
        XT = X.T
        # 方法一：根据公式求解
        S = np.cov(X)  # 两个维度之间协方差矩阵
        SI = np.linalg.inv(S)  # 协方差矩阵的逆矩阵
        # 马氏距离计算两个样本之间的距离，此处共有4个样本，两两组合，共有6个距离。
        n = XT.shape[0]
        d1 = []
        for i in range(0, n):
            for j in range(i + 1, n):
                delta = XT[i] - XT[j]
                d = np.sqrt(np.dot(np.dot(delta, SI), delta.T))
                d1.append(d)
        return d1

    # 点与点的堪培拉距离
    # num1:[1,2]
    # num2:[3,1]
    # return :[0.83333333]
    def canberra(self, num1, num2):
        import scipy.spatial.distance as dist
        import numpy as np

        return dist.pdist(np.array([num1, num2]), "canberra")

    def Bray_Curtis(self, num1, num2):
        import scipy.spatial.distance as dist
        import numpy as np

        return dist.partial(np.array([num1, num2]), "braycurtis")

    def Czekanowski(self, num1, num2):
        a1 = a2 = 0
        for i in range(0, len(num1)):
            if num1[i] > num2[i]:
                a1 = a1 + num2[i]
            else:
                a1 = a1 + num1[i]
        for i in range(0, len(num1)):
            a2 = a2 + ((num1[i]) ** 2) ** 0.5 + ((num2[i]) ** 2) ** 0.5
        return 1 - ((2 * a1) / a2)


# SMC Jaccard系数 符号属性变量 顺序变量
# 比例数值变量  混合类型变量
class coefficient:
    # smc
    def smc(self, num1, num2):
        a11 = a00 = a10 = a01 = 0
        for i in range(0, len(num1)):
            if num1[i] == num2[i] == 1:
                a11 += 1
            if num1[i] == num2[i] == 0:
                a00 += 1
            if num1[i] == 1 and num2[i] == 0:
                a10 += 1
            if num1[i] == 0 and num2[i] == 1:
                a01 += 1
        return (a11 + a00) / (a10 + a11 + a01 + a00)

    # jaccard系数
    def jaccard(self, num1, num2):
        a11 = a00 = a10 = a01 = 0
        for i in range(0, len(num1)):
            if num1[i] == num2[i] == 1:
                a11 += 1
            if num1[i] == num2[i] == 0:
                a00 += 1
            if num1[i] == 1 and num2[i] == 0:
                a10 += 1
            if num1[i] == 0 and num2[i] == 1:
                a01 += 1
        return a11 / (a11 + a10 + a01)

    # 符号属性变量
    def fuhao(self, num1, num2):
        a1 = a2 = 0
        for i in range(0, len(num1)):
            if num1[i] == num2[i]:
                a1 = a1 + 1
        return (len(num1) - a1) / len(num1)

    # 顺序变量
    def sunxu(self, num1):
        a1 = 0
        l = []
        l2 = []
        for i in num1:
            if i not in l:
                l.append(i)
        for i in range(1, len(l) + 1):
            l2.append(i)
        return l2
