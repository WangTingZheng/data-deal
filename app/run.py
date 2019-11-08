from app.mysql import *
from app.pub import *


def pub(item, limted):
    data = print_item(item, limted)
    res = []
    for i in data:
        res.append(float(i))
    sorted_nums = sorted_num(res)
    run_pub(sorted_nums)


pub("star", -1)
