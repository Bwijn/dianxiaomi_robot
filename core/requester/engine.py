from time import sleep
from bs4 import BeautifulSoup
from icecream import ic
import settings

import settings

import requests


def get_header():
    return {"None": None}
    # if
    #     cls.header


class Configurator:
    pass


def get_request_method():
    if settings.WHICHE_LIST == 1:
        return "post"
    return "get"


class Requester:
    """
    """
    __isinstance = None  # 单例

    # 当前的用户配置文件 dict
    user_config_dict = settings.CURRENT_CONFIG

    # 要请求的url
    # _todo_url = settings.CURRENT_CONFIG.get("todo_product").get("url")

    todoListNum = settings.WHICHE_LIST

    header = None

    # 单例 全局只返回同一个请求器
    def __new__(cls, *args, **kwargs):
        if cls.__isinstance:  # 如果被实例化了
            return cls.__isinstance  # 返回实例化对象
        cls.__isinstance = object.__new__(cls)  # 否则实例化
        return cls.__isinstance  # 返回实例化的对象

    def __init__(self):

        self.request_method = get_request_method()

    # def


    @classmethod
    def save_or_publish(cls, ):
        """
        保存产品 或 发布产品
        请求 url GET https://www.dianxiaomi.com/smtProduct/add.json 发送表单
        data字典里面 op =1 保存 =2 发布
        :param url:
        :return:
        """

        header_name = settings.CURRENT_CONFIG["save_header"]
        headers = header.Header(header_file_name=header_name)  # 更新请求头

        # form data
        from function_class.product_editor import ITEM_POST_DATA

        # ic(tem_data)
        count = 1
        while True:
            resp = requests.post(headers=headers.dict, data=ITEM_POST_DATA, url=cls.SAVE_OR_PUBLISH_URL, )
            print("第 [%d] 次发布 状态码：[%d]" % (count, resp.status_code))
            print("发布结果：\n", resp.text)
            if resp.status_code == 200:
                break
            count += 1
            sleep(10)
        # 提交的太频繁可能会出错，所以出错就立即抛出异常停止
        # if resp.status_code != 200:
        #     raise Exception("发布失败")

        return True

    @classmethod
    def request_item(cls, url) -> BeautifulSoup:
        """
        请求单个产品 处理后返回 bs4 对象
        https://www.dianxiaomi.com/smtProduct/edit.htm?id=46483711664692054 返回静态页面html
        :param url:
        :return:
        """
        # header_dict = header.handle_headers(header_str=header.get_item_edit_page_header)

        header_name = settings.CURRENT_CONFIG["edit.htm_header"]
        headers = header.Header(header_file_name=header_name)  # 更新请求头

        resp = requests.get(headers=headers.dict, url=url)
        # print(resp.text)
        # print("获取详情页状态码: [%d]" % resp.status_code)

        soup = BeautifulSoup(resp.text, "lxml")

        cls.GLOBAL_OBJ_BS4 = soup
        return soup
        # 测试时使用的，不用再去请求了，直接读取文件
        # with open("product_edit_page.txt", "r", encoding="utf-8") as f:  # 打开文件
        #     text = f.read()  # 读取文件
        #     # print(data)
        #     f.close()


# requester = Requester()

if __name__ == '__main__':
    requester.request()

    # def do_something(string):
    #     print("do_something", string)
    #     return BeautifulSoup("<a><a>", "lxml")
    #
    #
    # do_something(55)

    # filter_product()
    # print(1 and 2)

    # print(list_getter())
    # Requester().header.
    # r1 = Requester()
    # r2 = Requester()
    # print(id(r1), id(r2))
