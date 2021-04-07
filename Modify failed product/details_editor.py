"""

详情页编辑 类
包括：
1. 描述模板
2. 主图详情
3. 描述文字
"""
import copy
import json

import utils
from icecream import ic
import sku_creator

import form_data_handle


class DetailEditor(object):
    # def __init__(self,):

    with open("../json_cof/product_propertys.json", "r", encoding="utf-8") as f:  # 打开文件
        product_propertys = json.load(f)  # 读取文件
        f.close()
    with open("pc_detail.html", "r", encoding="utf-8") as f:  # 打开文件
        pc_text = f.read()  # 读取文件
        f.close()

    with open("../json_cof/mobile_details.json", "r", encoding="utf-8") as f:  # 打开文件
        text = json.load(f)  # 读取文件(dict)
        # ic(text)
        f.close()

    """
    手机端【详情】 编辑器类
    主要功能是编辑单独每一个产品的app端详情描述
    """

    def mobile_dict_add_describe_images(self, sku_image_list):
        """
        向mobile_describe.json 里面添加主图详情
        :return:
        """
        # 先复制再删除
        temporary_dict = {'style': {'hasMargin': False, 'height': '0', 'width': '0'},
                          'targetUrl': '',
                          'url': 'https://ae01.alicdn.com/kf/H9cf7d720bf2246a8b81eb1aa8138472fg/EARLFAMILY-13cm-x-6-6cm-for-Metal-Slug-X-Logo-Car-Stickers-Vinyl-Waterproof-Scratch-proof.jpg'}

        # 清零列表
        self.text['moduleList'][1]["images"] = []

        for image in sku_image_list:
            # ic(image)
            temporary_dict['url'] = image
            # ic(temporary_dict)
            self.text['moduleList'][1]["images"].append(temporary_dict.copy())

    def set_mobile_details(self, _in_dict, new_sku_info, images_url="unk;"):
        """
        传入的可能是一长串用 ;  分割的主图 所以要注意区分
        :param new_sku_info:
        :param _in_dict: 修改字典里的手机端描述
        :param images_url: 主图 url
        :param cls:
        :return:
        """

        # 传入skuImage list 将list中的缩略图拼入描述中去
        t_sku = sku_creator.temporary_sku_instance
        t_sku.sku_info = new_sku_info
        t_sku.sku_images_handle()

        t_sku.sku_image_list=[]
        # 如果skuImage里有图 则全放到手机描述中去
        if t_sku.sku_image_list:
            self.mobile_dict_add_describe_images(sku_image_list=t_sku.sku_image_list)
            # 改手机端详情主图
            # cls.text['moduleList'][1]["images"][0]['url'] = images_url  # 替换手机details主图
            _in_dict['mobileDetail'] = json.dumps(self.text)

        else:

            images_url = images_url.strip("'").split(";")
            images_url = images_url[0]  # 这个是单个主图
            temporary_dict = {'style': {'hasMargin': False, 'height': '0', 'width': '0'},
                              'targetUrl': '',
                              'url': 'https://ae01.alicdn.com/kf/H9cf7d720bf2246a8b81eb1aa8138472fg/EARLFAMILY-13cm-x-6-6cm-for-Metal-Slug-X-Logo-Car-Stickers-Vinyl-Waterproof-Scratch-proof.jpg'}
            self.text['moduleList'][1]["images"] = []  # 清零列表
            temporary_dict['url'] = images_url
            self.text['moduleList'][1]["images"].append(temporary_dict)  # 替换手机details主图
            ic(temporary_dict)
            ic(self.text)

    @classmethod
    def pc_details(cls, _in_dict, images_url="unk;"):
        # todo 之后填上主图
        images_url = images_url.strip("'").split(";")
        images_url = images_url[0]  # 这个是单个主图
        _in_dict['detail'] = cls.pc_text

    @classmethod
    def modify_product_propertys(cls, _in_dict):
        """
        修改品牌 和 自定义属性
        :param _in_dict:
        :return:
        """
        _in_dict['aeopAeProductPropertys'] = json.dumps(cls.product_propertys)


DetailEditor_instance = DetailEditor()

if __name__ == '__main__':
    sku_info = utils.load_json("../json_cof/sku2.json")
    # ic(sku_info)
    DetailEditor_instance.set_mobile_details(_in_dict=form_data_handle.data_dict, new_sku_info=sku_info)
