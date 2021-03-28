"""

详情页编辑 类
包括：
1. 描述模板
2. 主图详情
3. 描述文字
"""
import json


# from time import sleep


class DetailEditor(object):
    # def __init__(self,):

    with open("../json_cof/product_propertys.json", "r", encoding="utf-8") as f:  # 打开文件
        product_propertys = json.load(f)  # 读取文件
        f.close()
    with open("pc_detail.html", "r", encoding="utf-8") as f:  # 打开文件
        pc_text = f.read()  # 读取文件
        f.close()

    with open("../json_cof/mobile_details.json", "r", encoding="utf-8") as f:  # 打开文件
        text = json.load(f)  # 读取文件
        f.close()

    """
    手机端【详情】 编辑器类
    主要功能是编辑单独每一个产品的app端详情描述
    """

    @classmethod
    def editor(cls=None):
        print(cls)
        """

        :return:
        """
        print(cls.mro())

    @classmethod
    def change_mobile_details(cls, _in_dict, images_url="unk;"):
        """
        todo 目前只能上一个主图 可随时添加多个
        传入的可能是一长串用 ;  分割的主图 所以要注意区分
        :param _in_dict: 修改字典里的手机端描述
        :param images_url: 主图 url
        :param cls:
        :return:
        """

        images_url = images_url.strip("'").split(";")
        images_url = images_url[0]  # 这个是单个主图
        # 改手机端详情主图
        cls.text['moduleList'][1]["images"][0]['url'] = images_url  # 替换手机details主图
        _in_dict['mobileDetail'] = json.dumps(cls.text)
        # print("修改后的手机端json: ", cls.text)
        print("修改后的手机端json: ", _in_dict)

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


if __name__ == '__main__':
    test_url2 = "YYYYYYY;IIIIII;OOOOOOO"
    test_url = "https://ae01.alicdn.com/kf/HTB1atW6a98YBeNkSnb4q6yevFXaI/Three-Ratels-TZ-1200-17-1-15cm-1-4-pieces-border-collie-on-board-car-sticker.jpg;https://ae01.alicdn.com/kf/HTB1m3AEd1uSBuNjy1Xcq6AYjFXaJ/Three-Ratels-TZ-1200-17-1-15cm-1-4-pieces-border-collie-on-board-car-sticker.jpg;https://ae01.alicdn.com/kf/HTB1zZina5QnBKNjSZFmq6AApVXaA/Three-Ratels-TZ-1200-17-1-15cm-1-4-pieces-border-collie-on-board-car-sticker.jpg;https://ae01.alicdn.com/kf/HTB1hj.Gd25TBuNjSspmq6yDRVXaH/Three-Ratels-TZ-1200-17-1-15cm-1-4-pieces-border-collie-on-board-car-sticker.jpg;https://ae01.alicdn.com/kf/HTB1CvCiaZuYBuNkSmRyq6AA3pXa4/Three-Ratels-TZ-1200-17-1-15cm-1-4-pieces-border-collie-on-board-car-sticker.jpg;https://ae01.alicdn.com/kf/HTB1ge.gdYGYBuNjy0Foq6AiBFXaK/Three-Ratels-TZ-1200-17-1-15cm-1-4-pieces-border-collie-on-board-car-sticker.jpg"
    DetailEditor.change_mobile_details(images_url=test_url2, _in_dict={'mobileDetail': 1})
    # print(type(DetailEditor.editor()))
