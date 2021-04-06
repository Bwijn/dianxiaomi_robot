import json
import os
import re

import requests
from bs4 import BeautifulSoup
from icecream import ic

import sku_creator

import request_fun

os.environ['NO_PROXY'] = '1'  # 跳过系统代理


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

    # 标题长度限制128
    return subject[:128]


def extract_product_id(bs4_obj) -> str:
    bs4_obj = bs4_obj.find("input", id="productId")  # 找到这个标签的特征

    # print(soup)
    # 找到id
    xiaomi_id = bs4_obj.attrs['value']

    return xiaomi_id


def extract_shop_id(bs4_obj):
    pattern = re.compile(r"var shopId = (.*),")

    shopid = bs4_obj.find(text=pattern)
    shopid = pattern.search(shopid).group(1)

    return shopid


def extract_groupId_groupIds(bs4_obj):
    groupId = bs4_obj.find('input', id="groupId").attrs['value']
    groupIds = bs4_obj.find('input', id="groupIds").attrs['value']

    return groupId, groupIds
    # bs4_obj = bs4_obj.find()


def extract_freightTemplateId(bs4_obj):
    """
    todo 运费模板 待实现 异步获取 edit page 没有找到 freightTemplateId

    :param bs4_obj:
    :return:
    """
    pattern = re.compile(r"freightTemplateId = '(.*)',")

    freightTemplateId = bs4_obj.find(text=pattern)
    freightTemplateId = pattern.search(freightTemplateId).group(1)

    return freightTemplateId


def extract_source_url(bs4_obj):
    """
    提取详情页面的 来源 source_url （采集地址）
    :param bs4_obj:
    :return:
    """
    bs4_obj = bs4_obj.find("input", id="sourceUrl11")  # 找到这个标签的特征

    # 找到id
    source_url = bs4_obj.attrs['value']

    return source_url


def extract_sku_info(bs4_obj):
    bs4_obj = bs4_obj.find("input", id="aeopAeProductSKUs")  # 找到这个标签的特征
    sku_info = bs4_obj.attrs['value']

    sku_info = json.loads(sku_info)

    ic(sku_info)
    # print(type(sku_info))
    return sku_info


if __name__ == '__main__':
    t_url = "https://www.dianxiaomi.com/smtProduct/edit.htm?id=46483711700417334"

    rettt = request_fun.RequestPro.res_text(t_url)

    sku_info = extract_sku_info(rettt)

    sku_creator.SkuSetter(main_images="UNKNOW;", sku_info=sku_info)
