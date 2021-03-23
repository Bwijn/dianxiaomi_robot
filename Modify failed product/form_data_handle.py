import re
import json

# from processing_product import extract_product_subject, extract_main_image_url, extract_product_id
import processing_product

data = """id: 46483711645428674
shopId: 2451968
sourceUrl: https://www.aliexpress.com/item/32859527293.html?algo_pvid=67836406-a652-44f0-a020-1c69d974d8ee&algo_expid=67836406-a652-44f0-a020-1c69d974d8ee-35&btsid=0b86d81616158677257164337e81c5&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_
categoryId: 200000241
subject: Three Ratels TZ-1200 17.1*15cm 1-4 pieces border collie on board car sticker  stickers auto decals removable
aeopAeProductPropertys: [{"attrValueId":201512802,"attrNameId":2},{"attrValueId":9441741844,"attrNameId":219},{"attrValueId":200004814,"attrNameId":200000932},{"attrValueId":200004796,"attrNameId":6},{"attrValueId":31,"attrNameId":200000933},{"attrValueId":201447155,"attrNameId":200009171},{"attrValueId":439,"attrNameId":200000199},{"attrValueId":349907,"attrNameId":200000631},{"attrValueId":201447143,"attrNameId":200009169},{"attrValueId":201447146,"attrNameId":200009170},{"attrValueId":200000692,"attrNameId":200009168},{"attrValue":"Vinly","attrName":"Material Type"},{"attrValue":"Car Stickers","attrName":"Model Name"},{"attrValue":"Stickers and Decals","attrName":"Feature 1"},{"attrValue":"Laptop Sticker","attrName":"Feature 2"},{"attrValue":"Door Sticker","attrName":"Feature 3"},{"attrValue":"Window Sticker","attrName":"Feature 4"},{"attrValue":"Helmet Sticker","attrName":"Feature 5"},{"attrValue":"3D Car Stickers","attrName":"Feature 6"},{"attrValue":"Reflective Stickers","attrName":"Feature 8"},{"attrValue":"Black Silver Silvery","attrName":"Feature 9"},{"attrValue":"Cool and Creative","attrName":"Feature 10"},{"attrValue":"Hood Decals","attrName":"Feature 11"}]
motorIds: 
groupId: 10000000286948
groupIds: 10000000286948
imageURLs: https://ae03.alicdn.com/kf/He15f8581a93a4198be20110f505b0d05p.jpg;https://ae03.alicdn.com/kf/Hfbae4870c2b84e3dbc44e62930015e13S.jpg;https://ae03.alicdn.com/kf/H87de55f1ee1e4420bf748ab3c3179636m.jpg;https://ae03.alicdn.com/kf/Heb7c8d3e3043445d852d804e21982f50O.jpg;https://ae03.alicdn.com/kf/H7333035dfb4d423486ae1304450fbd79K.jpg
productUnit: 100000015
packageType: 0
lotNum: 
bulkOrder: 10
bulkDiscount: 30
aeopAeProductSKUs: [{"id":"200000182:193;5:100014064","ipmSkuStock":999,"skuPrice":"2.1","skuStock":true,"aeopSKUProperty":[{"propertyValueId":193,"skuImage":"https://ae03.alicdn.com/kf/He15f8581a93a4198be20110f505b0d05p.jpg","propertyValueDefinitionName":"","skuPropertyId":200000182,"themeVal":"颜色","attrVal":"黑色"},{"propertyValueId":100014064,"propertyValueDefinitionName":"8 cm","skuPropertyId":5,"themeVal":"尺寸","attrVal":"S"}],"skuCode":""},{"id":"200000182:193;5:361386","ipmSkuStock":999,"skuPrice":"2.9","skuStock":true,"aeopSKUProperty":[{"propertyValueId":193,"skuImage":"https://ae03.alicdn.com/kf/He15f8581a93a4198be20110f505b0d05p.jpg","propertyValueDefinitionName":"","skuPropertyId":200000182,"themeVal":"颜色","attrVal":"黑色"},{"propertyValueId":361386,"propertyValueDefinitionName":"12 cm","skuPropertyId":5,"themeVal":"尺寸","attrVal":"M"}],"skuCode":""},{"id":"200000182:193;5:361385","ipmSkuStock":999,"skuPrice":"4.1","skuStock":true,"aeopSKUProperty":[{"propertyValueId":193,"skuImage":"https://ae03.alicdn.com/kf/He15f8581a93a4198be20110f505b0d05p.jpg","propertyValueDefinitionName":"","skuPropertyId":200000182,"themeVal":"颜色","attrVal":"黑色"},{"propertyValueId":361385,"propertyValueDefinitionName":"20 cm","skuPropertyId":5,"themeVal":"尺寸","attrVal":"L"}],"skuCode":""}]
productPrice: 
deliveryTime: 7
wsValidNum: 30
reduceStrategy: payment_success_deduct
detail:  
grossWeight: 0.04
isPackSell: 0
baseUnit: 
addUnit: 
addWeight: 
packageLength: 25
packageWidth: 25
packageHeight: 1
promiseTemplateId: 0
freightTemplateId: 730183517
productMinPrice: 2.1
productMaxPrice: 4.1
sizechartId: 
activity: 
extraImages: 
aeopNationalQuoteConfiguration: {}
op: 1
isCheck: true
marketImg1: 
marketImg2: 
oldImgUrl: 
endTime: 
mobileDetail: 
dxmScheduleTimeStr: 
"""

data_dict = {}


def convert2dictionary(data_str=data) -> dict:
    """
    将字符串转换为字典
    :return: data
    """
    for line in data_str.splitlines():
        # print(line)
        key, value = line.split(': ', 1)
        if len(key) > 1:
            # print(line)
            data_dict[key] = value

    # add_details_of_mobile()

    return data_dict


def main_images_change(image_urls):
    # print(data_dict.items())
    data_dict['imageURLs'] = image_urls


def subject_change(subject):
    data_dict['subject'] = subject


def color_skus_change(main_images_url="UNKNOWN"):
    """
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

    # 替换thumbnail
    for i, val in enumerate(data):
        val['aeopSKUProperty'][0]['skuImage'] = main_images_url
        print(val)
    # print(data)
    # print(type(data))

    # 将 sku 替换为 修改完的 json文件
    data_dict[
        'aeopAeProductSKUs'] = data

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
    new_subject = processing_product.extract_product_subject(processing_product.GLOBAL_OBJ_BS4)
    new_main_image = processing_product.extract_main_image_url(processing_product.GLOBAL_OBJ_BS4)
    new_xiaomi_id = processing_product.extract_product_id(processing_product.GLOBAL_OBJ_BS4)
    new_source_url = processing_product.extract_source_url(processing_product.GLOBAL_OBJ_BS4)
    # 填充表单字典
    convert2dictionary(data_str=data)

    # 然后更换新的
    subject_change(new_subject)
    xiaomi_product_id_change(new_xiaomi_id)
    main_images_change(new_main_image)  # 更换主图
    color_skus_change(new_main_image)  # 更换sku小缩略图 仍使用主图
    # change_mobile_details(main_images_url=new_main_image)  # 更换手机端details 主图
    source_url_change(new_source_url)  # 更换source_url（采集地址）


# __all__ = [handle_form]
if __name__ == '__main__':
    convert2dictionary(data_str=data)
    # replace_product_all()
    # handle_form()
    # color_skus_change()
    change_mobile_details()
    print("替换如下：\n", data_dict)
