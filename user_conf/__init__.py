import os

from icecream import ic

from .module import PersonalConf

from .utils import load_file, handle_headers, post_data2dict

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

if __name__ == '__main__':
    pass
    # print(shao_kang.todo_header)

# JSON_TEMPLATE_PATH = CURRENT_PATH + r'\json_cof'
# FORM_DATA_PATH = CURRENT_PATH + r"\formdata"
# HEADER_CONFIG_PATH = CURRENT_PATH + r"\headers_config"


# shao_kang_dict = {
#     # 待发布的列表 字典配置
#     "todo_product": {
#         # 请求头
#         "header_cookie": HEADER_CONFIG_PATH + r"\get_product_list_header",
#         # 待发布    post表单 [300 itme/page]
#         "post_data": "pageNo=1&pageSize=300&shopId=-1&groupId=0&productStatusType=&dxmState=offline&dxmOfflineState=waitPublish&searchType=0&searchValue=&sortName=gmt_create&sortValue=&advancedSearch=&deliveryTimeLift=&deliveryTimeRight=&grossWeightLift=&grossWeightRight=&productCategory=&freightTemplateId=&timeLift=&timeRight=&advancedTime=1&commentType=0&commentContent=&sourceUrl=",
#         # [在线产品] or [已下架产品] or [待发布] 请求表单post_data不同而已
#         # "url": "https://www.dianxiaomi.com/smtProduct/pageList.htm",
#     },
#
#     "post_form": FORM_DATA_PATH + r"\post_form.txt",
#     "edit.htm_header": HEADER_CONFIG_PATH + r"\kang_single_item_header",  # 单个item的header
#     "save_header": HEADER_CONFIG_PATH + r"\kang_save_header",  # 保存的header
#     "custom_properties": JSON_TEMPLATE_PATH + r"\kang_product_propertys.json",  # 当前用户自定义产品属性
#     "sku_template_file": JSON_TEMPLATE_PATH + r"\sku_shao_kang.json",  # 价格、尺寸sku设置模板
# }
#
#
# _yao_yao1 = {
#     # 待发布的列表 字典配置
#     "todo_product": {
#         # 请求头
#         "header_cookie": HEADER_CONFIG_PATH + r"\yaoyao_todolist_header",
#         # 待发布    post表单 [300 itme/page]
#         "post_data": "pageSize=300&shopId=2461027&groupId=0&productStatusType=&dxmState=offline&dxmOfflineState=waitPublish",
#         # [在线产品] or [已下架产品] or [待发布] 请求表单post_data不同而已
#         "url": "https://www.dianxiaomi.com/smtProduct/pageList.htm",
#     },
#
#     "edit.htm_header": HEADER_CONFIG_PATH + r"\yaoyao_single_item",  # 单个item的header
#     "save_header": HEADER_CONFIG_PATH + r"\yaoyao_save_or_pub",  # 保存的header
#     "sku_template_file": JSON_TEMPLATE_PATH + r"\sku_shao_yaoyao.json",  # 价格设置模板-哪个sku模板
#     "post_form": FORM_DATA_PATH + r"\yaoyao_template_postdata",  # 当前用户的保存提交表单模板
#     "custom_properties": JSON_TEMPLATE_PATH + r"\yaoyao_propertys.json",  # 当前用户自定义产品属性
#
# }
# _yao_yao2 = {
#     # 待发布的列表 字典配置
#     "todo_product": {
#         # 请求头
#         "header_cookie": HEADER_CONFIG_PATH + r"\yaoyao2_todo_header",
#         # 待发布    post表单 [300 itme/page]
#         "post_data": "pageNo=1&pageSize=300&shopId=2545843&groupId=&productStatusType=&dxmState=offline&dxmOfflineState=waitPublish&searchType=0&searchValue=&sortName=&sortValue=&advancedSearch=&deliveryTimeLift=&deliveryTimeRight=&grossWeightLift=&grossWeightRight=&productCategory=&freightTemplateId=&timeLift=&timeRight=&advancedTime=1&commentType=0&commentContent=&sourceUrl=",
#         # [在线产品] or [已下架产品] or [待发布] 请求表单post_data不同而已
#         "url": "https://www.dianxiaomi.com/smtProduct/pageList.htm",
#     },
#
#     "edit.htm_header": HEADER_CONFIG_PATH + r"\yaoyao2_edit_ht",  # 单个item的header
#     "save_header": HEADER_CONFIG_PATH + r"\yaoyao2_save_or_pub",  # 保存的header
#     "post_form": FORM_DATA_PATH + r"\yaoyao2_template_postdata",  # 当前用户的保存提交表单模板
#
#     "sku_template_file": JSON_TEMPLATE_PATH + r"\sku_shao_yaoyao.json",  # 价格设置模板-哪个sku模板
#     "custom_properties": JSON_TEMPLATE_PATH + r"\yaoyao_propertys.json",  # 当前用户自定义产品属性
#
# }
#
# _yao_yao4 = {
#     # 待发布的列表 字典配置
#     "todo_product": {
#         # 请求头
#         "header_cookie": HEADER_CONFIG_PATH + r"\yaoyao4_todolist_header",
#         # 待发布    post表单 [300 itme/page]
#         "post_data": "pageNo=1&pageSize=300&shopId=2458782&groupId=0&productStatusType=&dxmState=offline&dxmOfflineState=waitPublish&searchType=0&searchValue=&sortName=gmt_create&sortValue=&advancedSearch=&deliveryTimeLift=&deliveryTimeRight=&grossWeightLift=&grossWeightRight=&productCategory=&freightTemplateId=&timeLift=&timeRight=&advancedTime=1&commentType=0&commentContent=&sourceUrl=",
#         # [在线产品] or [已下架产品] or [待发布] 请求表单post_data不同而已
#         "url": "https://www.dianxiaomi.com/smtProduct/pageList.htm",
#     },
#
#     "edit.htm_header": HEADER_CONFIG_PATH + r"\yaoyao4_edit_ht",  # 单个item的header
#     "save_header": HEADER_CONFIG_PATH + r"\yaoyao4_save_header",  # 保存的header
#     "post_form": FORM_DATA_PATH + r"\yaoyao4_post_data_template",  # 当前用户的保存提交表单模板
#     "sku_template_file": JSON_TEMPLATE_PATH + r"\sku_shao_yaoyao.json",  # 价格设置模板-哪个sku模板
#     "custom_properties": JSON_TEMPLATE_PATH + r"\yaoyao_propertys.json",  # 当前用户自定义产品属性
#
# }
