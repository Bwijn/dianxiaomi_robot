import settings


class RequestConf:
    def __init__(self,url,method,header,post_data=None):
        # 先确定url
        self.url = url
        # 再能确定请求方法
        self.method=method

        self.header = header
        self.post_data = post_data


