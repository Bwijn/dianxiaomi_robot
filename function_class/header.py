import utils


class Header(object, ):
    """
    todo 以后可以做成单例模式 但内存足够 目前不需要
    h=Header(xxxx)
    h.dict ={xxxxxxx}
    """
    path = '../headers_config/'

    def __init__(self, header_file_name):
        self.header_file_name = header_file_name
        self.path += self.header_file_name  # 拼接完整路径

    def __getattribute__(self, item):
        if item == 'dict':
            # 返回处理好的字典
            # print(self.path)
            self.header_str = utils.load_file(self.path)
            item = utils.handle_headers(header_str=self.header_str)
            return item
        else:
            return object.__getattribute__(self, item)


if __name__ == '__main__':
    # h = Header(header_file_name='get_item_edit_page_header')
    # print(h.dict)

    pass