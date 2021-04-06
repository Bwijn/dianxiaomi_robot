"""
修改发布失败的产品
eg： 修改sku的名字 (") 符号 改为 inches
"""

import os
import re
from time import sleep

import request_fun

os.environ['NO_PROXY'] = '1'  # 跳过系统代理


def find_item_url(bs4_obj=request_fun.RequestPro.get_list_page()):
    """
    bs4_obj=request_fun.RequestPro.get_list_page() 获取带发布列表
      将待发布的 每页100个产品的 edit url 分别列出来处理
      """

    # 找出当前页所有带有  'smtProduct/edit'  的标签
    soup = bs4_obj.find_all(limit=100, href=re.compile(r"smtProduct/edit"))
    print("共 %d 个产品需要修改: " % len(soup))
    for count, value in enumerate(soup, start=1):
        url_prefix = "https://www.dianxiaomi.com/"
        url_suffix = value.attrs['href']
        full_url = url_prefix + url_suffix

        print("正在修改第【%d】个产品" % count)

        print("产品url为：", full_url)

        # todo 这里之后设置成yield 生成器 解耦合
        # 分别请求处理
        request_fun.RequestPro.res_text(url=full_url)
        # request_fun.RequestPro.save_or_publish()
        # sleep(3)
        # break


if __name__ == '__main__':
    find_item_url()
