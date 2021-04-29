# from icecream import ic
#
# import settings
# from function_class import utils
#
#
# class DataStorage:
#     # 当前用户的post_formpath
#
#     current_form_data_path = settings.CURRENT_CONFIG["post_form"]
#     with open(current_form_data_path, 'r', encoding='utf-8') as f:
#         data_dict = f.read()
#
#         data_dict = utils.handle_headers(data_dict)  # 转换为字典
#         f.close()
#
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         """
#         单例返回同一个字典
#         :param args:
#         :param kwargs:
#         """
#         if cls.data_dict:
#             return cls.data_dict
#         else:
#             raise Exception("!!!!!!")
#
#
# # 全局form data
# ITEM_POST_DATA = DataStorage()
# if __name__ == '__main__':
#     a = DataStorage()
#     a['aeopAeProductPropertys'] = 1
#     ic(a)
#     # ic(a)
#
#     b = DataStorage()
#     ic(b)
#     # ic(b)
