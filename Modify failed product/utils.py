import json

# data_dict = {}


def load_file_wrapper(file_name, ):
    """
        带参数装饰器 添加打开文件读取功能
        :return:
    """

    def decorated(func):
        def wrapper(*args, **kwargs):
            with open(file_name, "r", encoding="utf-8") as f:  # 打开文件
                form_text = json.load(f)  # 读取文件
                f.close()
            return func(*args, **kwargs)

        return wrapper

    return decorated


def load_file(file_name, ):
    print(type(file_name))
    with open(file_name, "r", encoding="utf-8") as f:  # 打开文件
        form_text = f.read()  # 读取文件
        f.close()
    return form_text


def handle_headers(header_str):
    """
    将header字符串转换为字典
    :param header_str:
    :return:
    """
    internal_dict = {}
    for line in header_str.split('\n'):
        temp_list = line.split(': ', 1)
        if len(temp_list) == 2:
            key, value = temp_list
            internal_dict[key] = value

        # key = key.strip("\n")
        # print(line)
    # print(internal_dict)
    return internal_dict

# def convert2dictionary(data_str=form_text) -> dict:
#     """
#     将字符串转换为字典 装饰器
#     :return: data
#     """
#
#     for line in data_str.split('\n'):
#         temp_list = line.split(': ', 1)
#         if len(temp_list) == 2:
#             key, value = temp_list
#             data_dict[key] = value
#
#     # add_details_of_mobile()
#
#     return data_dict
