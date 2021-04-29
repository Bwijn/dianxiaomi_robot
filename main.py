"""
启动函数
"""

from icecream import ic
import time
from core.item import ProductItem
from core import get_products, submit
from core.product_editor import editor


def run():
    """
    启动脚本编辑产品
    :return:
    """

    # 获取产品列表 pageList -> <"class", "bs4.Beautiful">
    productList = get_products()
    # ic(productList)
    for num, soup in enumerate(productList, start=1):
        """
        for 循环 遍历处理列表 
        """
        # ic(count,item)
        print("当前\033[1;32;40m正在编辑\033[0m第【%d】个产品" % num)

        # 单个产品对象
        product_item = ProductItem(soup=soup)

        # 编辑产品
        editor.edit_product(product=product_item)

        time.sleep(10)

        # 提交表单 保存
        submit(product=product_item)

        time.sleep(25)
        # break


if __name__ == '__main__':
    run()
