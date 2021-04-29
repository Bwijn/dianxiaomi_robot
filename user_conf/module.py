import os

from icecream import ic

from .utils import *


class BaseConf:
    """
    每个人都有的设置
    """
    # add.json 保存或上货的api
    SAVE_OR_PUBLISH_URL = "https://www.dianxiaomi.com/smtProduct/add.json"

    GET_PRODUCT_LIST_URL = "https://www.dianxiaomi.com/smtProduct/pageList.htm"
    CONF_FILE_PATH = os.path.dirname(__file__)



    # 目前所有人通用pc模板


    PC_DESCRIBE_TMPL = load_file(file_name=r"C:\Users\bwijn\PycharmProjects\pythonProject\user_conf\kangkang\pc_detail.html")

    # 通用mobile模板
    MOBILE_TMPL = None


class PersonalConf(BaseConf):
    # 待发布列表的请求头
    # 待发布列表的

    def __init__(
            self,
            self_folder_name,
            todo_post_data,
            post_template,
            todo_header,
            get_item_header,
            save_header,
            item_properties,
            sku_template,
    ):
        # json
        self.sku_template = sku_template
        self.item_properties = item_properties

        # header
        self.save_header = save_header
        self.todo_header = todo_header
        self.get_item_header = get_item_header

        # data
        self.post_template = post_template
        self.todo_post_data = todo_post_data

        # 当前用户文件夹名
        self.self_folder_name = self_folder_name

        # 无线端模板
        self.mobile_tmpl = load_json(
            file_name=r"C:\Users\bwijn\PycharmProjects\pythonProject\user_conf\kangkang\mobile_tmpl.json")

        # 转化操作
        self.conversion()

    def absolute_path(self, file_name):
        """
        拼接绝对路径
        :param file_name:
        :return:
        """
        full_path = self.CONF_FILE_PATH + "/" + self.self_folder_name + "/" + file_name
        return full_path

    def process_header(self, header_file_name):
        """

        :param header_file_name: 传入header文件名
        :return: header Dict
        """
        # 变为绝对路径
        absolute_header_path = self.absolute_path(file_name=header_file_name)

        # 转化为header字典
        header_content = load_file(absolute_header_path)
        header_dict = handle_headers(header_content)
        return header_dict

    def process_json(self, json_name):
        # 变为绝对路径
        absolute_header_path = self.absolute_path(file_name=json_name)
        json_obj = load_json(absolute_header_path)
        return json_obj

    def conversion(self):
        """
        将文件名转换成可用的Python对象
        :return:
        """
        # 转换为post字典
        self.todo_post_data = post_data2dict(post_data=self.todo_post_data)
        # ic(self.todo_post_data)

        # 转换为header dict
        self.todo_header = self.process_header(self.todo_header)
        # ic(self.todo_header)

        self.get_item_header = self.process_header(self.get_item_header)
        # ic(self.get_item_header)

        self.post_template = self.process_header(self.post_template)
        # ic(self.post_template)

        self.sku_template = self.process_json(self.sku_template)
        # ic(self.sku_template)

        self.item_properties = self.process_json(self.item_properties)

        self.save_header = self.process_header(self.save_header)


if __name__ == '__main__':
    shao_kang = PersonalConf(
        self_folder_name="kangkang",
        todo_header="get_product_list_header",
        todo_post_data="pageNo=1&pageSize=300&shopId=-1&groupId=0&productStatusType=&dxmState=offline&dxmOfflineState=waitPublish&searchType=0&searchValue=&sortName=gmt_create&sortValue=&advancedSearch=&deliveryTimeLift=&deliveryTimeRight=&grossWeightLift=&grossWeightRight=&productCategory=&freightTemplateId=&timeLift=&timeRight=&advancedTime=1&commentType=0&commentContent=&sourceUrl=",

        post_template="post_form.txt",
        get_item_header="kang_single_item_header",
        item_properties="kang_product_propertys.json",
        save_header="kang_save_header",
        sku_template="sku_shao_kang.json",
    )

    # ic(shao_kang.mobile_tmpl)
    ic(os.getcwd())

    # 父目录

    ic(os.path.abspath(parent))
    ic(shao_kang.CONF_FILE_PATH)