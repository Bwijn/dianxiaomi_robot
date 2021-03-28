import re
import json
import utils

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
    # print(data_dict.items())
    image_urls=image_urls.strip("'").split(';')[0]
    data_dict['imageURLs'] = image_urls


def subject_change(subject):
    data_dict['subject'] = subject


def skus_change(main_images_url="UNKNOWN"):
    """
    修改sku 添加sku小缩略图
    替换 color_name 的选择小图 直接用第一个主图url就可以
    通过正则表达式替换 因为 目标dict是一个字符串 ↓
    "aeopSKUProperty":[{"propertyValueId":193,"skuImage":"xxx","。。。。

    :return:
    """

    # 这里要将多个主图切割成一个主图
    # 因为采集来的可能有多个主图,所以需要切割为1个
    main_images_url = main_images_url.strip("'").split(";")
    main_images_url = main_images_url[0]  # 这个是单个主图

    # 这里读取json文件，修改json
    with open('sku_variant.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        f.close()

    # 替换thumbnail
    for i, val in enumerate(data):
        val['aeopSKUProperty'][0]['skuImage'] = main_images_url
        # print(val)
    # print("读取的sku的信息",json.dumps(indent=2,obj=data))

    # 将 sku 替换为 修改完的 json文件
    data_dict[
        'aeopAeProductSKUs'] = json.dumps(indent=2, obj=data)

    # print("sku修改后：：：\n",data)

    return None


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


def replace_product_all():
    """
    替换新的 subject、sku_image、price、xiaomi_id、
    :return:
    """

    # 打开每一个详情页获取里面新的 subject、sku_image、price、xiaomi_id、
    new_subject = processing_product.extract_product_subject(request_fun.RequestPro.GLOBAL_OBJ_BS4)
    new_main_image = processing_product.extract_main_image_url(request_fun.RequestPro.GLOBAL_OBJ_BS4)
    new_xiaomi_id = processing_product.extract_product_id(request_fun.RequestPro.GLOBAL_OBJ_BS4)
    new_source_url = processing_product.extract_source_url(request_fun.RequestPro.GLOBAL_OBJ_BS4)

    # 然后更换新的
    subject_change(new_subject)  # 换标题
    xiaomi_product_id_change(new_xiaomi_id)  # 换xiaomi id
    main_images_change(new_main_image)  # 更换主图
    skus_change(new_main_image)  # 更换sku及缩略图 --仍使用主图

    details_editor.DetailEditor.change_mobile_details(images_url=new_main_image, _in_dict=data_dict)  # 更换手机端details 主图
    details_editor.DetailEditor.pc_details(images_url=new_main_image, _in_dict=data_dict)  # 更换PC端details 主图
    details_editor.DetailEditor.modify_product_propertys(_in_dict=data_dict)  # 更换品牌等自定义属性
    source_url_change(new_source_url)  # 更换source_url（采集地址）


if __name__ == '__main__':
    pass
