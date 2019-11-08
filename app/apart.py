# apart string in list according char
# string: likes 2: 3, 4: 2, 1: 1, 3: 1, 5: 1, 7: 1,
# char: likes ","
# return: ['2:3', '4:2', '1:1', '3:1', '5:1', '7:1']
def apart(string, char):
    tmp = ""
    res = []
    for i in string:
        if i == char:
            tmp = tmp.replace(" ", "")
            res.append(tmp)
            tmp = ""
        else:
            tmp += i
    return res
