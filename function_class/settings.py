import os

os.environ['NO_PROXY'] = '1'  # 跳过系统代理

OP_CODE_STATE = 1  # 1保存 2发布


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



    # 已下架产品 post表单 [300 itme/page]
    # "product_list_post_data": "pageNo=1&pageSize=300&shopId=-1&groupId=&productStatusType=offline&dxmState=online&dxmOfflineState=&searchType=0&searchValue=&sortName=&sortValue=&advancedSearch=&deliveryTimeLift=&deliveryTimeRight=&grossWeightLift=&grossWeightRight=&productCategory=&freightTemplateId=&motorState=0&timeLift=&timeRight=&advancedTime=1&commentType=0&commentContent=&sourceUrl=",

    # 待发布    post表单 [300 itme/page]
    "product_list_post_data": "pageNo=1&pageSize=300&shopId=-1&groupId=0&productStatusType=&dxmState=offline&dxmOfflineState=waitPublish&searchType=0&searchValue=&sortName=gmt_create&sortValue=&advancedSearch=&deliveryTimeLift=&deliveryTimeRight=&grossWeightLift=&grossWeightRight=&productCategory=&freightTemplateId=&timeLift=&timeRight=&advancedTime=1&commentType=0&commentContent=&sourceUrl=",

    # [在线产品] or [已下架产品] or [待发布] 请求表单post_data不同而已
    "product_list": "https://www.dianxiaomi.com/smtProduct/pageList.htm",

}
