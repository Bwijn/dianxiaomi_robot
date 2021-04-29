import json

import settings


def edit_mobile(product):
    # 要添加的图片 sku缩略图没有就上主图
    img_list = product.skuImageList if product.skuImageList else product.main_images
    # 无线端模板
    mobile_tmpl = settings.CURRENT_CONFIG.mobile_tmpl.copy()

    # 描述片段
    snippet_tmpl = {'style': {'hasMargin': False, 'height': '0', 'width': '0'},
                    'targetUrl': '',
                    'url': 'https://ae01.alicdn.com/kf/H9cf7d720bf2246a8b81eb1aa8138472fg/EARLFAMILY-13cm-x-6-6cm-for-Metal-Slug-X-Logo-Car-Stickers-Vinyl-Waterproof-Scratch-proof.jpg'}

    # 初始化无线端模板
    mobile_tmpl['moduleList'][1]["images"] = []

    # 无线端模板里面添加图片
    for json_snippet in img_list:
        # 描述列表
        editor = mobile_tmpl['moduleList'][1]["images"]
        snippet_tmpl['url'] = json_snippet
        # ic(temporary_dict)
        editor.append(snippet_tmpl.copy())

    # 保存 字符串形式
    product.form_data['mobileDetail'] = json.dumps(mobile_tmpl)