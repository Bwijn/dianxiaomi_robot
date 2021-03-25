import json
import os
import re

import requests
from bs4 import BeautifulSoup

import header

# from form_data_handle import data_dict, replace_product_all
import form_data_handle

os.environ['NO_PROXY'] = '1'  # 跳过系统代理

SAVE_OR_PUBLISH_URL = "https://www.dianxiaomi.com/smtProduct/add.json"

# 请求单个详情页的解析后的bs4对象
GLOBAL_OBJ_BS4 = ''
GLOBAL_DETAIL_TEXT = ""


def res_text(url):
    """
    返回静态页面html
    :param url:
    :return:
    """
    header_dict = header.handle_headers(header_str=header.get_item_edit_page_header)
    # print("RES_TEXT 内部 url为：%s\ndict: %s" % (url, header_dict))

    resp = requests.get(headers=header_dict, url=url)
    print(resp.text)
    print("获取详情页 状态码: [%d]" % resp.status_code)

    global GLOBAL_OBJ_BS4, GLOBAL_DETAIL_TEXT


    soup = BeautifulSoup(resp.text, "lxml")

    # GLOBAL_DETAIL_TEXT = resp.text
    GLOBAL_OBJ_BS4 = soup

    # 测试时使用的，不用再去请求了，直接读取文件
    # with open("product_edit_page.txt", "r", encoding="utf-8") as f:  # 打开文件
    #     text = f.read()  # 读取文件
    #     # print(data)
    #     f.close()


def extract_main_image_url(bs4_obj):
    """
    抽取 url <script> 标签中的 主图 地址 也可用于单个Color skus 的图片 eg: 黑色
    最后的结果可能是用；分割的一串好几个url:
    url;url;url...

    :return:
    """
    # raise Exception

    pattern = re.compile(r"var imageURLs = (.*),")

    # bs4_obj= bs4_obj.find("var imageURLs")

    main_images_list = bs4_obj.find(text=pattern)
    main_images_list = pattern.search(main_images_list).group(1).strip("'")

    print("抽取到新的 main_images:\n", main_images_list)

    return main_images_list


def extract_product_subject(bs4_obj) -> str:
    """
    提取新标题
    :param bs4_obj:
    :return: str 提取到的标题
    """

    bs4_obj = bs4_obj.find("input", autocomplete="off")  # 找到这个标签的特征

    # 找到标题
    subject = bs4_obj.attrs['value']

    print("抽取到新的 subject:\n", subject)
    return subject


def extract_product_id(bs4_obj) -> str:
    bs4_obj = bs4_obj.find("input", id="productId")  # 找到这个标签的特征

    # print(soup)
    # 找到id
    xiaomi_id = bs4_obj.attrs['value']

    print("抽取到新的 id:\n", xiaomi_id)

    return xiaomi_id


def extract_source_url(bs4_obj):
    """
    提取详情页面的 来源 source_url （采集地址）
    :param bs4_obj:
    :return:
    """
    bs4_obj = bs4_obj.find("input", id="sourceUrl11")  # 找到这个标签的特征

    # print(bs4_obj)
    print("来源url：", bs4_obj.attrs['value'])
    # 找到id
    source_url = bs4_obj.attrs['value']

    return source_url


def save_or_publish(url=SAVE_OR_PUBLISH_URL):
    """
    保存产品 或 发布产品
    请求 url GET https://www.dianxiaomi.com/smtProduct/add.json 发送表单
    data字典里面 op =1 保存 =2 发布
    :param url:
    :return: res.text 返回给控制台 要监控的!!!
    """
    headers = header.handle_headers(header_str=header.save_or_publish_header)  # 更新请求头

    form_data_handle.replace_product_all()  # 更新请求表单
    tem_data = form_data_handle.data_dict

    resp = requests.post(headers=headers, data=tem_data, url=SAVE_OR_PUBLISH_URL, )
    print("发布状态码：", resp.status_code)
    print("发布结果：\n", resp.text)
    return True


if __name__ == '__main__':

    res_text('https://www.dianxiaomi.com/smtProduct/edit.htm?id=46483711665250168')

    #
    # with open("product_edit_page.txt", mode='r', encoding='utf-8')as f:
    #     text = f.read()
    #
    # pattern = re.compile(r"var imageURLs = (.*),")
    #
    # new_bs4_obj = BeautifulSoup(text, 'lxml')
    # print(new_bs4_obj.find(text=pattern))
    #
    # extract_main_image_url(new_bs4_obj)
    # pass
