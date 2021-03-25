"""
修改发布失败的产品
eg： 修改sku的名字 (") 符号 改为 inches
"""
from bs4 import BeautifulSoup  # +++++++++++++++++++++

import os
import re
from time import sleep
import requests

import header
import processing_product

os.environ['NO_PROXY'] = '1'  # 跳过系统代理

# 获取待上货的列表
Pending_URL = "https://www.dianxiaomi.com/smtProduct/list.htm"


def get_list_page(url=Pending_URL):
    """
    自动获取待发布列表
    :return:
    """
    form_data = {
        "shopId": '-1',
        "groupId": '0',
        "productStatusType": "",
        "dxmState": "offline",
        "dxmOfflineState": "waitPublish",
    }

    temp_header = header.handle_headers(header_str=header.get_product_list_header)

    resp = requests.post(headers=temp_header, data=form_data, url=Pending_URL)

    # print("发布结果：\n", resp.text)
    # print("发布状态码：", resp.status_code)
    soup = BeautifulSoup(resp.text, "lxml")
    return soup


def find_item_url(bs4_obj=get_list_page()):
    """
      将待发布的 每页100个产品的 edit url 分别列出来处理
      """

    # 找出当前页所有带有  'smtProduct/edit'  的标签
    soup = bs4_obj.find_all(limit=100, href=re.compile("smtProduct/edit"))
    print("共 %d 个产品需要修改: " % len(soup))
    for count, value in enumerate(soup, start=1):
        url_prefix = "https://www.dianxiaomi.com/"
        url_suffix = value.attrs['href']
        full_url = url_prefix + url_suffix

        print("正在修改第【%d】个产品" % count)

        print("产品url为：", full_url)

        # todo 这里之后设置成yield 生成器 解耦合
        # 分别请求处理
        processing_product.res_text(url=full_url)
        processing_product.save_or_publish()
        sleep(3)


if __name__ == '__main__':
    find_item_url()

    # get_list_page()

    # with open("pc_detail.html", 'r', encoding='utf-8')as f:
    #     text = f.read()

    # soup = BeautifulSoup(text, 'lxml')
    # soup = soup.find_all(limit=100, href=re.compile("smtProduct/edit"))
    # print("共 %d 个产品需要修改: " % len(soup))
    # for count, value in enumerate(soup, start=1):
    #     url_prefix = "https://www.dianxiaomi.com/"
    #     url_suffix = value.attrs['href']
    #     full_url = url_prefix + url_suffix
    #
    #     print("正在修改第【%d】个产品" % count)
    #
    #     print("产品url为：", full_url)
    #
    #     # processing_product.res_text(url='https://www.dianxiaomi.com/smtProduct/edit.htm?id=46483711665250168')
    #     processing_product.res_text(url=full_url)
    #     break
