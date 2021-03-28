class Header(object, ):
    def __init__(self, header_file_name):
        self.header_file_name = header_file_name

        self.header_str = ''

        self.load_file()

    # hh = ''

    def load_file(self):
        folder_path = '../headers_config/'
        file_nam = self.header_file_name
        full_file_name = folder_path + file_nam
        with open(full_file_name, "r", encoding="utf-8") as f:  # 打开文件
            self.header_str = f.read()

    @staticmethod
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


if __name__ == '__main__':
    h = Header('get_item_edit_page_header')
    h_dict=h.handle_headers(h.header_str)
    print(type(h_dict))
    # print(a)
    # h.load_file()
    # print(Header('get_item_edit_page_header').header_str)

    # h.handle_headers(h.header_str)
    # print(h.header_str)
