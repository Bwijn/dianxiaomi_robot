import form_data_handle
import json
import utils
from icecream import ic
import copy

ic.configureOutput()

SKU_TEMPLATE_PATH = "../json_cof/"


def sku_images_handle(current_pro_sku):
    """
    提取产品的skuImage
    :return: 返回skuImage的可迭代对象
    """
    sku_image_list = []  # 最后要返回的skuImage的列表
    current_pro_sku=json.loads(current_pro_sku)
    # with open("../json_cof/sku2.json", "r", encoding="utf-8") as f:  # 打开文件
    #     current_pro_sku = json.load(f)
    #     f.close()

    # 抽取skuImage 对比set() 得出 各个颜色缩略图url
    # 然后根据url来分别添加尺寸
    # 抽取主图
    # todo 之后可以改为从html中用正则表达式获取url
    for sku_dict in current_pro_sku:

        for sku_pro_item in sku_dict['aeopSKUProperty']:
            skuimage = sku_pro_item.get('skuImage', )
            if skuimage:
                sku_image_list.append(skuimage)

    sku_image_list = set(sku_image_list)
    # sku_image_list = ['^' * 50]
    return sku_image_list
    # ic(len(sku_image_list))
    # ic(sku_image_list)


def skus_setting(sku_images, sku_template_name="sku_template.json"):
    """
    更改skus的算法 skuimage 然后分别设置三个尺寸
    :param sku_template_name: 要用那个sku模板
    :param sku_images: 处理好的skuImage的URL list
    :return: 返回一个sku字符串 或 json列表
    """

    result_json_list = []

    sku_template_name = SKU_TEMPLATE_PATH + sku_template_name
    # 要设置的尺寸和定价
    template_sku_json = utils.load_json(sku_template_name)

    # 根据模板写好的框架进行增删改查
    for i, val in enumerate(sku_images, start=1):
        # ic(i, val)
        template_sku_json[0]['aeopSKUProperty'][0]['skuImage'] = val
        template_sku_json[1]['aeopSKUProperty'][0]['skuImage'] = val
        template_sku_json[2]['aeopSKUProperty'][0]['skuImage'] = val

        # 这里使用深拷贝来防止引用
        result_json_list.extend(copy.deepcopy(template_sku_json))

        # 将每个都添加到 RESULT_LIST 中
    # print(json.dumps(result_json_list, ensure_ascii=False))
    # ic(len(result_json_list))


def sku_handle(*args, **kwargs):
    """
    sku 智能处理
    :param kwargs:
    :return:
    """
    # ic(kwargs)
    # ic(args)
    # exit()

    sku_info = kwargs.get('sku_info', None)
    images_set = sku_images_handle(current_pro_sku=sku_info)
    skus_setting(sku_images=images_set)

    return None


if __name__ == '__main__':
    pass
    # skus_change()
    # sku_images_handle()

    sku_handle(123)
    # skus_setting(sku_images_handle())
