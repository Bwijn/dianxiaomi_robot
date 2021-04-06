import requests
from bs4 import BeautifulSoup
from icecream import ic

import form_data_handle

from header import Header

from init_config import kang as k


class RequestPro(object):
    """
    Pro 有 process / professional 的意思😘
    """

    # Pending_URL = "https://www.dianxiaomi.com/smtProduct/offline.htm?dxmState=offline&dxmOfflineState=publishFail&shopId=-1"

    # add.json 保存或上货的api
    SAVE_OR_PUBLISH_URL = "https://www.dianxiaomi.com/smtProduct/add.json"

    # 全局bs4对象
    GLOBAL_OBJ_BS4 = None

    @classmethod
    def get_list_page(cls, url=k.get("product_list")):
        """
        获取待发布列表
        :return:
        """

        headers = Header('get_product_list_header')  # 更新请求头

        if url.find("list.htm") != -1:
            resp = requests.post(headers=headers.dict, data=k.get("To be released_form_data"),
                                 url=url)

        else:
            resp = requests.get(headers=headers.dict, data=k.get("To be released_form_data"),
                                url=url)

        # print("请求list结果：\n", resp.text)
        # print("请求list状态码：", resp.status_code)
        soup = BeautifulSoup(resp.text, "lxml")
        return soup

    @classmethod
    def save_or_publish(cls, url=SAVE_OR_PUBLISH_URL):
        """
        保存产品 或 发布产品
        请求 url GET https://www.dianxiaomi.com/smtProduct/add.json 发送表单
        data字典里面 op =1 保存 =2 发布
        :param url:
        :return: res.text 返回给控制台 要监控的!!!
        """
        # headers = header.handle_headers(header_str=header.save_or_publish_header)

        headers = Header('save_or_publish_header')  # 更新请求头

        form_data_handle.replace_product_all()  # 更新请求表单
        tem_data = form_data_handle.data_dict

        # ic(tem_data)
        resp = requests.post(headers=headers.dict, data=tem_data, url=cls.SAVE_OR_PUBLISH_URL, )
        print("发布状态码：", resp.status_code)
        print("发布结果：\n", resp.text)
        return True

    @classmethod
    def res_text(cls, url) -> BeautifulSoup:
        """
        请求单个产品 处理后返回 bs4 对象
        https://www.dianxiaomi.com/smtProduct/edit.htm?id=46483711664692054 返回静态页面html
        :param url:
        :return:
        """
        # header_dict = header.handle_headers(header_str=header.get_item_edit_page_header)

        headers = Header('get_item_edit_page_header')  # 更新请求头

        resp = requests.get(headers=headers.dict, url=url)
        # print(resp.text)
        print("获取详情页 状态码: [%d]" % resp.status_code)

        soup = BeautifulSoup(resp.text, "lxml")

        cls.GLOBAL_OBJ_BS4 = soup
        return soup
        # 测试时使用的，不用再去请求了，直接读取文件
        # with open("product_edit_page.txt", "r", encoding="utf-8") as f:  # 打开文件
        #     text = f.read()  # 读取文件
        #     # print(data)
        #     f.close()
