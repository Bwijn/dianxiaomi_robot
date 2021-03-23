

"""
requests url  https://www.dianxiaomi.com/smtProduct/add.json
上架新产品

"""


import os

import requests
# from cookie_handle import handle_cookie
from post_header import handle_headers
from form_handle import handle_form

os.environ['NO_PROXY'] = '1'  # 跳过系统代理

data_dic = handle_form()
headers_dict = handle_headers()
# print(data_dic)
POST_URL = "https://www.dianxiaomi.com/smtProduct/add.json"



if __name__ == "__main__":

    resp = requests.post(headers=headers_dict, data=data_dic, url=POST_URL, )
    print(resp.status_code)
    print(resp.text)
    print(resp.headers)
