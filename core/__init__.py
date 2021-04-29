from time import sleep

from bs4 import BeautifulSoup

from icecream import ic
from .requester import RequestConf, request
import settings
from .tool import *

user = settings.CURRENT_CONFIG


def has_class_but_no_id(tag):
    return tag.has_attr('data-id') and tag.has_attr('data-cid')


@filter_(out_args="目前这个参数还没用-_-!")
def get_products(_requester=requester) -> list:
    """
    :param _requester:
    :return:
    """
    # if WHICHE_LIST == 1:
    # url = settings.CURRENT_CONFIG.

    # 设置请求配置

    # url
    url = user.GET_PRODUCT_LIST_URL
    header = user.todo_header
    post_data = user.todo_post_data

    # ic(url,header,post_data)
    todoList_conf = RequestConf(url=url, method="post", header=header, post_data=post_data)
    res = _requester.request(todoList_conf)

    soup = BeautifulSoup(res.text, "lxml")
    productList = soup.find_all(has_class_but_no_id)
    print("\033[1;32;40m当前产品共【%d】个\033[0m" % len(productList))

    return productList


def submit(product):
    data = product.form_data
    url = user.SAVE_OR_PUBLISH_URL
    headers = user.save_header

    conf = RequestConf(url=url, method="post", header=headers, post_data=data)

    # ic(tem_data)
    count = 1
    while True:
        resp = request(request_conf=conf)
        print("第 [%d] 次发布 状态码：[%d]" % (count, resp.status_code))
        print("发布结果：\n", resp.text)
        if resp.status_code == 200:
            break
        count += 1
        sleep(10)


if __name__ == '__main__':
    list_getter()
