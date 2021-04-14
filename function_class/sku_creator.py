"""
根据缩略图的个数来填充sku 没有color 缩略图，则
style A .................
"""

import form_data_handle
import json
import utils
from icecream import ic
import copy

ic.configureOutput()

SKU_TEMPLATE_PATH = "../json_cof/"


def sku_images_handle(sku_info, sku_image_list):
    """
    提取产品的skuImage
    :return: 返回skuImage的可迭代对象
    """

    if not isinstance(sku_info, list):
        # 判断一下是不是list 不是的话先转成list再操作
        sku_info = json.loads(sku_info)

    # 然后根据url来分别添加尺寸
    # 抽取主图
    # todo 之后可以改为从html中用正则表达式获取url
    for sku_dict in sku_info:
        for sku_pro_item in sku_dict['aeopSKUProperty']:
            skuImage = sku_pro_item.get('skuImage', )
            if skuImage:
                sku_image_list.append(skuImage)


class SkuSetter(object, ):
    """

    """

    def __init__(self, sku_info, main_images="unknown", sku_template_name='sku_template.json'):
        self.main_images = main_images  # 主图 没有skuimage时备用
        self.sku_info = sku_info  # 传入的 skuinfo dianxiaomi HTML里面的<input value=.....>
        self.sku_template_name = SKU_TEMPLATE_PATH + sku_template_name  # sku模板路径
        self.sku_image_list = list()  # 最后去重后的 skuImage list
        self.template_sku_json = utils.load_json(self.sku_template_name)  # sku模板
        # self.sku_images_handle()  # 执行skuImage搜集 得出列表
        self.result_json_list = []  # 最终要提交的json列表

        self.zippedList = None  # 元组列表

        # DefinitionName 自定义名称取代 “黑色” “白色”
        self.propertyValueDefinitionName = ["style A", "style B", "style C", "style D", "style E", "style F", "style G",
                                            "style H",
                                            "style I", "style J", "style K", "style L", "style M", "style N", ]
        self.propertyValueId_color = [771,175,173,496,350686,1052,29, 691, 10, 350852, 366, 193]
        self.attrVal = ["米黄色","绿色","蓝色","紫色","棕色","粉色","白色", "灰色", "红色", "橙色", "黄色", "黑色",]
        self.propertyValueId_size = []
        self.id = "200000182:193;5:100014064"

        # 创建一个实例后就执行sku设置 -- 执行操作函数
        # self.skus_setting()  # post表单里修改sku项

    def sku_images_handle(self):
        """
        提取产品的skuImage
        :return: 返回skuImage的可迭代对象
        """

        if not isinstance(self.sku_info, list):
            # 判断一下是不是list 不是的话先转成list再操作
            self.sku_info = json.loads(self.sku_info)

        # 然后根据url来分别添加尺寸
        # 抽取主图
        # todo 之后可以改为从html中用正则表达式获取url
        for sku_dict in self.sku_info:
            # 下架列表中 sku的信息不一样 直接结束处理skuImage 直接把列表清零 单一主图
            if self.sku_info[0].get("aeopSKUProperty", None) is None:
                self.sku_image_list = []
                return
            for sku_pro_item in sku_dict['aeopSKUProperty']:
                skuimage = sku_pro_item.get('skuImage', )
                if skuimage:
                    self.sku_image_list.append(skuimage)

        # 抽取skuImage set去重 得出 各个颜色缩略图url
        self.sku_image_list = list(set(self.sku_image_list))

        # ic(len(self.sku_image_list))
        # ic(self.sku_image_list)
        # return list(sku_image_list)

    def skus_setting(self):
        """
        更改skus的算法 skuimage 然后分别设置三个尺寸
        """
        self.sku_images_handle()  # 先填充sku_images_list

        # 通过zip函数将skuImage列表和style X 等变更属性打包成一个元组列表分别修改
        self.zippedList = zip(self.sku_image_list, self.propertyValueDefinitionName, self.propertyValueId_color,
                              self.attrVal)
        self.zippedList = list(self.zippedList)
        # ic(self.zippedList)

        # 分情况来进行sku设定
        # 1.如果有skuImage缩略图就正常用template sku 拼补
        if self.sku_image_list:
            # 根据模板写好的框架进行增删改查 改每个SKU 里面的[skuImage,propertyValueDefinitionName,id,propertyValueId,attrVal]
            self.set_sku()  # 设置sku细节
            self.sku_id_splicing()  # 设置sku id
            # ic(self.result_json_list)

            self.final_modification_submission_form()  # 最后向post表单里填充
            return



        # 2.如果sku_images长度为0 就代表取1个主图做skuImage
        else:
            main_images = self.main_images.strip("'").split(";")[0]
            self.template_sku_json[0]['aeopSKUProperty'][0]['skuImage'] = main_images
            self.template_sku_json[1]['aeopSKUProperty'][0]['skuImage'] = main_images
            self.template_sku_json[2]['aeopSKUProperty'][0]['skuImage'] = main_images

            # ic(self.template_sku_json)
            # 最后替换提交表单form里的sku项
            form_data_handle.data_dict["aeopAeProductSKUs"] = json.dumps(self.template_sku_json)
            # ic("没有skuImage - 单主图sku：", template_sku_json)
            return None

    def set_sku(self):
        # 清空最终列表 保证无误
        self.result_json_list = []
        # 根据模板写好的框架进行增删改查 改每个SKU 里面的[skuImage,propertyValueDefinitionName,id,propertyValueId,attrVal]
        # ic(self.zippedList)
        for val in self.zippedList:
            # 设置缩略图
            self.template_sku_json[0]['aeopSKUProperty'][0]['skuImage'] = val[0]
            self.template_sku_json[1]['aeopSKUProperty'][0]['skuImage'] = val[0]
            self.template_sku_json[2]['aeopSKUProperty'][0]['skuImage'] = val[0]

            # 设置自定义颜色属性
            self.template_sku_json[0]['aeopSKUProperty'][0]['propertyValueDefinitionName'] = val[1]
            self.template_sku_json[1]['aeopSKUProperty'][0]['propertyValueDefinitionName'] = val[1]
            self.template_sku_json[2]['aeopSKUProperty'][0]['propertyValueDefinitionName'] = val[1]
            # 设置propertyValueId_color
            self.template_sku_json[0]['aeopSKUProperty'][0]['propertyValueId'] = val[2]
            self.template_sku_json[1]['aeopSKUProperty'][0]['propertyValueId'] = val[2]
            self.template_sku_json[2]['aeopSKUProperty'][0]['propertyValueId'] = val[2]

            # 设置attrVal
            self.template_sku_json[0]['aeopSKUProperty'][0]['attrVal'] = val[3]
            self.template_sku_json[1]['aeopSKUProperty'][0]['attrVal'] = val[3]
            self.template_sku_json[2]['aeopSKUProperty'][0]['attrVal'] = val[3]

            # 这里使用深拷贝来防止引用

            self.result_json_list.extend(copy.deepcopy(self.template_sku_json))

    def sku_id_splicing(self):
        # 设置id
        for i in self.result_json_list:
            self.temp_colorid = i['aeopSKUProperty'][0]['propertyValueId']
            self.temp_sizeid = i['aeopSKUProperty'][1]['propertyValueId']

            self.temp_sizeid, self.temp_colorid = list(map(str, [self.temp_sizeid, self.temp_colorid]))

            # ic(self.temp_sizeid,self.temp_colorid)
            self.id = "200000182:" + self.temp_colorid + ";5:" + self.temp_sizeid
            i['id'] = self.id
            i['id'] = self.id
            i['id'] = self.id

    def final_modification_submission_form(self):
        # 最后替换提交表单form里的sku项
        form_data_handle.data_dict["aeopAeProductSKUs"] = json.dumps(self.result_json_list)
        # ic(self.result_json_list)
        # 结束sku设置


# temporary_sku_instance = SkuSetter(main_images="1", sku_info="1", )

if __name__ == '__main__':
    # t_sku.sku_image_list = [1, 2, 3]
    # ic(t_sku.sku_image_list)

    skuinfo = utils.load_json(file_name="../json_cof/sku2.json")
    sku = SkuSetter(main_images='1', sku_info=skuinfo)
    sku.sku_images_handle()
    sku.skus_setting()
