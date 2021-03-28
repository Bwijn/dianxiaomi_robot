import re
import json

import processing_product
import details_editor
import request_fun

data = """
id: 46483711665250160
shopId: 2499851
sourceUrl: https://www.aliexpress.com/item/1005002102203560.html?algo_pvid=136210ee-35ee-42db-9de6-21e62d2529fb&algo_expid=136210ee-35ee-42db-9de6-21e62d2529fb-15&btsid=0b86d80216165658156311347e59e8&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_
categoryId: 200000241
subject: Funny Car Sticker Paws Up Pitbull Bully Dog Decal KK Vinyl Decor Black/Silver Sunscreen Waterproof 16cmX8cm
aeopAeProductPropertys: 自定义属性和品牌属性等
motorIds: 
groupId: 
groupIds: 
imageURLs: https://ae01.alicdn.com/kf/H205d87aa2a964e8aaaf17c6762cecae5w/Funny-Car-Sticker-Paws-Up-Pitbull-Bully-Dog-Decal-KK-Vinyl-Decor-Black-Silver-Sunscreen-Waterproof.jpg;https://ae01.alicdn.com/kf/H80635e44c1fd4b61ace0822cda028508f/Funny-Car-Sticker-Paws-Up-Pitbull-Bully-Dog-Decal-KK-Vinyl-Decor-Black-Silver-Sunscreen-Waterproof.jpg
productUnit: 100000015
packageType: 0
lotNum: 
bulkOrder: 10
bulkDiscount: 30
aeopAeProductSKUs: sku信息
productPrice: 
deliveryTime: 7
wsValidNum: 30
reduceStrategy: payment_success_deduct
grossWeight: 0.04
isPackSell: 0
baseUnit: 
addUnit: 
addWeight: 
packageLength: 25
packageWidth: 25
packageHeight: 1
promiseTemplateId: 0
freightTemplateId: 729734421
productMinPrice: 2.9
productMaxPrice: 4.5
sizechartId: 
activity: 
extraImages: 
aeopNationalQuoteConfiguration: {}
op: 2
isCheck: true
marketImg1: 
marketImg2: 
oldImgUrl: 
endTime: 
dxmScheduleTimeStr:  
"""

data_dict = {}


def convert2dictionary(data_str=data) -> dict:
    """
    将字符串转换为字典
    :return: data
    """
    for line in data_str.split('\n'):
        temp_list = line.split(': ', 1)
        if len(temp_list) == 2:
            key, value = temp_list
            data_dict[key] = value

    # add_details_of_mobile()

    return data_dict


def main_images_change(image_urls):
    # print(data_dict.items())
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


def change_pc_details():
    with open("pc_detail.html", "r", encoding="utf-8") as f:  # 打开文件
        text = f.read()  # 读取文件
        # print(data)
        f.close()

    data_dict['detail'] = text


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
    # 填充表单字典
    convert2dictionary()

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
    convert2dictionary(data_str=data)
    print(data_dict)
