"""
这个模块将一个form表单作为模板 然后在其基础上进行修改
"""
import re
import json

from bs4 import BeautifulSoup
from icecream import ic

import sku_creator
import utils
import settings
import processing_product
import details_editor
import request_fun

# 这里读取json文件，修改json
with open('../formdata/post_form.txt', 'r', encoding='utf-8') as f:
    data_dict = f.read()
    data_dict = utils.handle_headers(data_dict)  # 转换为字典
    # print(json.dumps(data_dict, indent=4, ensure_ascii=False))
    # print(data_dict)
    # exit(1131)
    f.close()


def main_images_change(image_urls):
    """
    只放一个主图 因为其他主图中可能有其他品牌和地域信息
    :param image_urls:
    :return:
    """
    # print(data_dict.items())
    image_urls = image_urls.strip("'").split(';')[0]
    data_dict['imageURLs'] = image_urls


def subject_change(subject):
    data_dict['subject'] = subject


def xiaomi_product_id_change(xiaomi_id):
    """
    id: 46483711626580414
    像这样的 dianxiaomi_id 号
    :param xiaomi_id:
    :return:
    """
    data_dict['id'] = xiaomi_id


def source_url_change(source_url):
    """

    :param source_url:
    :return:
    """
    data_dict['sourceUrl'] = source_url


def shop_id_change(shopid):
    """

    :param source_url:
    :return:
    """
    data_dict['shopId'] = shopid


def op_state_code_change():
    data_dict['op'] = settings.OP_CODE_STATE


def replace_product_all():
    """
    替换新的 subject、sku_image、price、xiaomi_id、
    :return:
    """

    # 提取采集的产品的 各种信息 eg: 标题、来源url、主图url
    new_subject = processing_product.extract_product_subject(request_fun.RequestPro.GLOBAL_OBJ_BS4)
    new_main_image = processing_product.extract_main_image_url(request_fun.RequestPro.GLOBAL_OBJ_BS4)
    new_xiaomi_id = processing_product.extract_product_id(request_fun.RequestPro.GLOBAL_OBJ_BS4)
    new_source_url = processing_product.extract_source_url(request_fun.RequestPro.GLOBAL_OBJ_BS4)
    new_shop_id = processing_product.extract_shop_id(request_fun.RequestPro.GLOBAL_OBJ_BS4)
    new_sku_info = processing_product.extract_sku_info(request_fun.RequestPro.GLOBAL_OBJ_BS4)

    # print("new_subject:{}\n"
    #       "new_main_image:{}\n"
    #       "new_xiaomi_id:{}\n"
    #       "new_source_url:{}\n"
    #       "new_shop_id:{}\n"
    #       "new_sku_info:{}\n".format(new_subject, new_main_image, new_xiaomi_id, new_source_url, new_shop_id,
    #                                  new_sku_info))

    # 然后更换新的属性 ------------------------------------------------------------------------------
    subject_change(new_subject)  # 换标题
    xiaomi_product_id_change(new_xiaomi_id)  # 换店小蜜专有id
    main_images_change(new_main_image)  # 更换主图
    op_state_code_change()  # 操作状态 保存或发布 随setting.py [OP_CODE_STATE]变化
    # 更换sku及缩略图 --仍使用主图
    sku_creator.SkuSetter(main_images=new_main_image, sku_info=new_sku_info).skus_setting()

    details_editor.DetailEditor.pc_details(images_url=new_main_image, _in_dict=data_dict)  # 更换PC端details和主图
    details_editor.DetailEditor.modify_product_propertys(_in_dict=data_dict)  # 更换品牌等自定义属性

    # __________________________________________________________________________________________________________________________________
    # 更换手机端的描述主图
    details_editor.DetailEditor_instance.set_mobile_details(_in_dict=data_dict, new_sku_info=new_sku_info,
                                                            images_url=new_main_image)

    source_url_change(new_source_url)  # 更换source_url（采集地址）


if __name__ == '__main__':
    print(json.dumps(data_dict, indent=4, ensure_ascii=False))