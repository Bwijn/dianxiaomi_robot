import re
import json

from icecream import ic
from .replace_func import *




class Extractor:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        product_item = args[0]
        # ic(self.product_item)

        # 填充产品信息
        self.fill_new_info(product=product_item)

    def fill_new_info(*args, **kwargs):
        """
        替换新的 subject、sku_image、price、xiaomi_id ...
        :return:
        """

        # product_item 实例对象
        product = kwargs["product"]

        # product 信息表单
        product_data_form = product.form_data

        # product page soup
        item_page = product.info_bs4

        # 提取采集的产品的 各种信息 eg: 标题、来源url、主图url
        new_subject = extract_product_subject(item_page)
        new_main_image = extract_main_image_url(item_page)
        new_xiaomi_id = extract_product_id(item_page)
        new_source_url = extract_source_url(item_page)
        opcode = settings.OP_CODE_STATE

        # 然后更换新的属性 ------------------------------------------------------------------------------
        subject_change(form_data=product_data_form, subject=new_subject)  # 换标题
        xiaomi_product_id_change(form_data=product_data_form, xiaomi_id=new_xiaomi_id)  # 换店小蜜专有id
        main_images_change(image_urls=new_main_image, form_data=product_data_form)  # 更换主图
        source_url_change(form_data=product_data_form, source_url=new_source_url)  # 更换source_url（采集地址）
        op_state_code_change(form_data=product_data_form, opcode=opcode)  # 操作状态 保存或发布 随setting.py [OP_CODE_STATE]变化

        return None
        # sku_info = extract_sku_info()
        # product.
        # return

        # skuImageList = sku_creator.SkuSetter(sku_info=new_sku_info)
        # 获取skuImageList
        # skuImageList = skuImageList.skuimage_extraction()

        # 更换sku及缩略图 --仍使用主图
        sku_creator.SkuSetter(main_images=new_main_image, sku_info=new_sku_info).skus_setting(*args, **kwargs)

        # 更换PC端details和主图
        details_editor.DetailEditor.pc_details(images_url=new_main_image, skuImageList=skuImageList,
                                               _in_dict=pe.ITEM_POST_DATA)

        # 更换品牌等自定义属性
        details_editor.DetailEditor.modify_product_propertys(_in_dict=pe.ITEM_POST_DATA)

        # 更换手机端的描述主图
        details_editor.DetailEditor_instance.set_mobile_details(_in_dict=pe.ITEM_POST_DATA, new_sku_info=new_sku_info,
                                                                images_url=new_main_image)


extractor = Extractor()
if __name__ == '__main__':
    extractor(1)
    # ic(extractor.product_item)
    # t_url = "https://www.dianxiaomi.com/smtProduct/edit.htm?id=46483711700417334"
    #
    # rettt = request_fun.RequestPro.res_text(t_url)
    #
    # sku_info = extract_sku_info(rettt)
    #
    # sku_creator.SkuSetter(main_images="UNKNOW;", sku_info=sku_info)
    pass
