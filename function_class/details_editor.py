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

import settings


class DetailEditor(object):
    # def __init__(self,):
    pc_detais_html = "../source_text_information/pc_detail.html"

    # 对应每个用户的自定义属性
    custom_properties = "../json_cof/" + settings.CURRENT_CONFIG["custom_properties"]
    with open(custom_properties, "r", encoding="utf-8") as f:  # 打开文件
        product_propertys = json.load(f)  # 读取文件
        f.close()

    with open(pc_detais_html, "r", encoding="utf-8") as f:  # 打开文件
        pc_text = f.readlines()  # 读取文件

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
        t_sku = sku_creator.SkuSetter(sku_info=new_sku_info, )
        # 创建新的实例对象去处理new_sku_info =>得出skuImage_list
        t_sku.skuimage_extraction()
        # t_sku.sku_image_list => 这是最后处理的skuImage

        # 如果skuImage_list里有图 则全放到手机描述中去
        if t_sku.sku_image_list:
            self.mobile_dict_add_describe_images(sku_image_list=t_sku.sku_image_list)
            # 改手机端详情主图
            # cls.text['moduleList'][1]["images"][0]['url'] = images_url  # 替换手机details主图
            _in_dict['mobileDetail'] = json.dumps(self.text)

        else:  # 没有的话只能用一个主图了 -_-!
            images_url = images_url.strip("'").split(";")
            images_url = images_url[0]  # 这个是单个主图
            temporary_dict = {'style': {'hasMargin': False, 'height': '0', 'width': '0'},
                              'targetUrl': '',
                              'url': 'https://ae01.alicdn.com/kf/H9cf7d720bf2246a8b81eb1aa8138472fg/EARLFAMILY-13cm-x-6-6cm-for-Metal-Slug-X-Logo-Car-Stickers-Vinyl-Waterproof-Scratch-proof.jpg'}
            self.text['moduleList'][1]["images"] = []  # 清零列表
            temporary_dict['url'] = images_url
            self.text['moduleList'][1]["images"].append(temporary_dict.copy())  # 替换手机details主图
            _in_dict['mobileDetail'] = json.dumps(self.text)

    @classmethod
    def pc_details(cls, _in_dict, skuImageList, images_url="unk;"):

        # 主图
        images_url = images_url.strip("'").split(";")[0]

        # 如果没有skuImage则用主图
        describe_imageList = skuImageList if skuImageList else [images_url]

        # TAG IMG<img>
        img_tag = """<img src="" style="box-sizing: border-box; padding: 0px; margin: 0px; border-style: none; 
        vertical-align: middle; max-width: 100%;" /> """

        # 深拷贝一份读取的描述列表 readlines
        details_readlines = copy.deepcopy(cls.pc_text)

        # 依次插入到html中
        for url_item in describe_imageList:
            complete_string = img_tag[:10] + url_item + img_tag[10:]
            # ic(complete_string)
            # print(complete_string)
            details_readlines.insert(27, complete_string)
            details_readlines.insert(27, "\n")

        # ic(details_readlines)
        pc_text = "".join(details_readlines)

        # print(describe_imageList, images_url, pc_text)

        # 保存大字典里面 todo 1111!!!
        _in_dict['detail'] = pc_text

    @classmethod
    def modify_product_propertys(cls, _in_dict):
        """
        修改品牌 和 自定义属性
        :param _in_dict:
        :return:
        """
        _in_dict['aeopAeProductPropertys'] = json.dumps(cls.product_propertys)

    @classmethod
    def insert_img(cls, details_list):

        pass


DetailEditor_instance = DetailEditor()

if __name__ == '__main__':
    DetailEditor.pc_details(_in_dict={},
                            skuImageList=["$$$$$$$", "{}{}{}NNNNNNNNNNNNNNNN", '&&&&&&&&&&&&7'],
                            images_url="((((((((((((((((;")
    # DetailEditor.pc_details(_in_dict={})
    # DetailEditor_instance.set_mobile_details(_in_dict=form_data_handle.data_dict, new_sku_info=sku_info)

    pass
