"""
修改发布失败的产品
eg： 修改sku的名字 (") 符号 改为 inches
"""
import os
import re
from time import sleep

import requests

from header import handle_headers
import processing_product

os.environ['NO_PROXY'] = '1'  # 跳过系统代理

URL = "https://www.dianxiaomi.com/smtProduct/offline.htm?dxmState=offline&dxmOfflineState=publishFail&shopId=-1"
# data_dic = handle_form()
# headers_dict = handle_headers()

# resp = requests.get(headers=headers_dict, url=URL)

# print(resp.text, end="\n\n\n\n\n")
# print(resp.status_code)


from bs4 import BeautifulSoup  # +++++++++++++++++++++

if __name__ == '__main__':

    """
    将待发布的 每页100个产品的 edit url 分别列出来处理
    """

    with open("product_list.txt", "r", encoding="utf-8") as f:  # 打开文件
        data = f.read()  # 读取文件
        # print(data)

    soup = BeautifulSoup(data, "lxml")

    # 找出当前页所有带有  'smtProduct/edit'  的标签
    soup = soup.find_all(limit=100, href=re.compile("smtProduct/edit"))
    print("共 %d 个产品需要修改: " % len(soup))

    for count, value in enumerate(soup, start=1):
        url_prefix = "https://www.dianxiaomi.com/"
        url_suffix = value.attrs['href']
        full_url = url_prefix + url_suffix

        print("正在修改第【%d】个产品" % count)

        print("产品url为：", full_url)

        # 分别打开每个产品详细 然后处理
        processing_product.res_text(url=full_url)
        processing_product.save_or_publish()
        # print("当前产品信息修改完毕")
        sleep(2)
        break
