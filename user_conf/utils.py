
import json

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
    # print(type(file_name))
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


# json文件转list
def load_json(file_name):
    with open(file_name, "r", encoding="utf-8") as f:  # 打开文件
        text = json.load(f)  # 读取文件
        f.close()
    return text


# &连接的post data 转字典
def post_data2dict(post_data):
    # post 表单数据 转换字典
    post_data = post_data.split("&")
    str_dic = dict()
    for i in post_data:
        key = i.split("=")[0]
        val = i.split("=")[1]
        str_dic[key] = val

    return str_dic


if __name__ == '__main__':
    pass