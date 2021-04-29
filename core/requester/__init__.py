import requests
from icecream import ic
from .conf import RequestConf


def request(request_conf) -> requests.Response:
    """
    请求操作
    :return:
    """
    # ic(request_conf.method,request_conf.header,request_conf.url)

    if request_conf.method == "post":
        resp = requests.post(headers=request_conf.header, data=request_conf.post_data,
                             url=request_conf.url, )
        # ic(resp.text)
        return resp

    elif request_conf.method == "get":
        resp = requests.get(headers=request_conf.header,
                            url=request_conf.url, )
        # ic(resp.text)
        return resp

    else:
        raise Exception("请求方法错误")

    # # 待发布列表
    # if self.todoListNum == 1:
    #     request_cof = self.user_config_dict["todo_product"]
    #
    #     headers = header.Header(request_cof["header_cookie"])  # 请求头暂时通用没毛病
    #     temp_data = request_cof["post_data"]
    #     temp_url = request_cof["url"]
    #     # ic(11111111)
    #
    #     # ic(resp.status_code)
    #
    # elif settings.WHICHE_LIST == 5:
    #     text = utils.load_file(
    #         r"C:\Users\bwijn\PycharmProjects\pythonProject\source_text_information\demo_待发布.html")
    #     soup = BeautifulSoup(text, "lxml")
    #     return soup
    # else:
    #     print("product_list 不正确 查修！！！")
    #     exit(00000000000)
    #     return None

    # print("请求list结果：\n", resp.text)
    # print("请求list状态码：", resp.status_code)
