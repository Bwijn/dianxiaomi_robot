from icecream import ic
from .extractor import extractor
from .sku_setter import editSKU
from .pc_editor import edit_pc
from .mobile_editor import edit_mobile
import settings


class Editor:
    pass

    def __init__(self, product_ite=1):
        pass
        # 传入的item
        # self.product_item = product_item

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def edit_product(self, product):
        """
               编辑产品

        product_item: 单个item对象 <tr>...</tr>
        :return:None
        """

        # 单个产品编辑入口url
        # ic(product_item.edit_page_url)
        # exit()

        # 编辑产品信息
        # 提取填充新产品信息
        extractor(product)

        # 设置sku
        editSKU(product=product)


        # 检查否是多ps
        # MultiPieces = check_multi_pieces(product_item)

        # mobile
        edit_mobile(product=product)
        # pc
        edit_pc(product=product)


        return None


def check_multi_pieces(product):
    """
    判断是否多个ps
    :param product_item:
    :return:
    """
    temp = product_item.find(string=re.compile("[0-9][pP][Ss]"))
    # ic(temp,product_item)
    if temp:
        # ic(product_item)
        # ic(temp)
        return temp.string  # '2ps'
    return None


# 创建编辑器对象
editor = Editor()
