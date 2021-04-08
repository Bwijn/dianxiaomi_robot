import re

from icecream import ic

kang = {  # 4.5折 -55%
    'edit_page': 'get_item_edit_page_header',
    'pro_list': 'get_product_list_header',
    'post_header': 'save_or_publish_header',

    "To be released_form_data": {
        "shopId": '-1',  # -1全部店铺 如果写上详细的就是分店
        "groupId": '0',
        "productStatusType": "",
        "dxmState": "offline",
        "dxmOfflineState": "waitPublish",
    },

    "product_list_post_data":"pageSize=300&shopId=-1&groupId=0&productStatusType=offline&dxmState=online&dxmOfflineState=&searchType=0&searchValue=&sortName=gmt_create&sortValue=&advancedSearch=&deliveryTimeLift=&deliveryTimeRight=&grossWeightLift=&grossWeightRight=&productCategory=&freightTemplateId=&timeLift=&timeRight=&shelvesKinds=-1&motorState=0&advancedTime=1&commentType=0&commentContent=&sourceUrl=",
    # "product_list": "https://www.dianxiaomi.com/smtProduct/list.htm",  # 获取待上货的列表
    # "product_list": "https://www.dianxiaomi.com/smtProduct/offline.htm?dxmState=offline&dxmOfflineState=publishFail&shopId=-1",
    "product_list": "https://www.dianxiaomi.com/smtProduct/pageList.htm",

}

# failed = kang['product_list']
# failed=failed.find('list.htm')
# if failed:
#     ic(failed)
