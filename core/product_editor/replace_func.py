"""
这个模块将一个form表单作为模板 然后在其基础上进行修改
"""
import json
import re

from icecream import ic

import settings


def main_images_change(form_data, image_urls):
    """
    只放一个主图 因为其他主图中可能有其他品牌和地域信息
    :param form_data:
    :param image_urls:
    :return:
    """
    # print(pe.ITEM_POST_DATA.items())
    image_urls = image_urls.strip("'").split(';')[0]
    form_data['imageURLs'] = image_urls


def subject_change(form_data, subject):
    form_data["subject"] = subject


def xiaomi_product_id_change(form_data, xiaomi_id):
    """
    像这样的 dianxiaomi_id 号
    :param form_data:
    :param xiaomi_id: 46483711626580414
    :return:
    """
    form_data['id'] = xiaomi_id


def source_url_change(form_data, source_url):
    """

    :param form_data:
    :param source_url:
    :return:
    """
    form_data['sourceUrl'] = source_url

# 目前不需要这个函数替换，因为都包含在postdata里面
# def shop_id_change(shopid):
#     """
#
#     :param source_url:
#     :return:
#     """
#     pe.ITEM_POST_DATA['shopId'] = shopid


def op_state_code_change(form_data, opcode):
    form_data["op"] = opcode
    return


def extract_main_image_url(item_page):
    """
    抽取 url <script> 标签中的 主图 地址 也可用于单个Color skus 的图片 eg: 黑色
    最后的结果可能是用；分割的一串好几个url:
    url;url;url...

    :return:
    """
    # raise Exception

    pattern = re.compile(r"var imageURLs = (.*),")

    main_images_list = item_page.find(text=pattern)
    main_images_list = pattern.search(main_images_list).group(1).strip("'")

    return main_images_list


def extract_product_subject(item_page) -> str:
    """
    提取新标题
    :param item_page: soup
    :return: str 提取到的标题
    """

    item_page = item_page.find("input", autocomplete="off")  # 找到这个标签的特征

    # 找到标题
    subject = item_page.attrs['value']

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


def extract_source_url(bs4_obj):
    """
    提取详情页面的 来源 source_url （采集地址）
    :param bs4_obj:
    :return:
    """

    # 两种情况 找到那个用那个
    source_url_input_tag1 = bs4_obj.find("input", id="sourceUrl11")  # 找到这个标签的特征

    source_url_input_tag2 = bs4_obj.find("input", id="sourceUrl10")  # 找到这个标签的特征

    # 找到id
    bs4_obj = source_url_input_tag1 if source_url_input_tag1 else source_url_input_tag2
    source_url = bs4_obj.attrs['value']

    return source_url


def extract_sku_info(bs4_obj):
    bs4_obj = bs4_obj.find("input", id="aeopAeProductSKUs")  # 找到这个标签的特征
    sku_info = bs4_obj.attrs['value']

    # ic(sku_info)
    sku_info = json.loads(sku_info)

    return sku_info


def modify_product_property(form_data, custom_properties):
    """
    修改品牌 和 自定义属性
    :return:
    """

    form_data['aeopAeProductPropertys'] = json.dumps(custom_properties)


if __name__ == '__main__':
    print(json.dumps(pe.ITEM_POST_DATA, indent=4, ensure_ascii=False))
    pass
