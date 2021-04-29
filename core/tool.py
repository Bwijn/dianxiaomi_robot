"""
# 过滤产品列表中已经编辑过的 或者多pieces项 2PS / 4PS / 8PS
"""
import re

from bs4 import BeautifulSoup
from icecream import ic

import settings


def has_class_but_no_id(tag):
    """
    bs4 查找过滤函数
    :param tag:
    :return:
    """
    return tag.has_attr('data-id') and tag.has_attr('data-cid')


def edited(product):
    mode = settings.FILTER_STATE

    # 判断传入的对象是不是 <class 'bs4.BeautifulSoup'> 是不是list
    # if not isinstance(self._bs4_obj, list) and not self._bs4_obj:
    #     raise Exception("当前传入的 %s 对象" % self._bs4_obj)
    # elif self._bs4_obj == 1 and self._bs4_obj is None:
    #     raise Exception("需要传入 %s 的 soup对象" % BeautifulSoup.__name__)
    # else:
    #     soup = self._bs4_obj.find(cid="productList", )
    #     soup = soup.find_all(has_class_but_no_id)

    # 是否执行过滤操作 过滤已经编辑好的
    # filtering_mode == 1 过滤已经编辑好的
    if mode == 1:
        pattern = re.compile(r"[Ss]tyle \w/[12][0-9]")
        result = product.find(string=pattern)
        if not result:
            return product
    else:
        raise Exception("未填写过滤模式！！！")


def filter_(out_args):
    """
    过滤产品列表的装饰器
    :param out_args:
    :return:
    """

    def wrapper(func):
        def inner(*args, **kwargs):
            productList = func(*args, **kwargs)  # [<tr1>,<tr2>...]

            # productList = soup.find_all(string="编辑", href=re.compile(r"smtProduct/edit"))
            # 处理此处的soup对象 过滤其中已经编辑好的item返回一个干净的list

            result = list(filter(edited, productList))

            # 差值
            difference = len(productList) - len(result)
            print("当前产品列表已经有【%d】个\033[1;32;40m完成编辑\033[0m已从产品列表剔除" % difference)

            print("当前\033[1;32;40m未编辑\033[0m产品共【%d】个，需要修改" % len(result))

            return result  # result 过滤后的结果列表

        return inner

    return wrapper


if __name__ == '__main__':
    # ic(__name__)

    text = load_file(r"C:\Users\bwijn\PycharmProjects\pythonProject\source_text_information\demo_待发布.html")
    # print(text)
    p = Product_filter(bs4_obj=BeautifulSoup(text, "lxml")).filter_product()
    # ic(p)
