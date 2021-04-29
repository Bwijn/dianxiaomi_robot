import os
from user_conf import (shao_kang)

os.environ['NO_PROXY'] = '1'  # 跳过系统代理

# 店小蜜请求间隔全局设定
# PASS PASS

CURRENT_CONFIG = shao_kang  # 当前用户 对象 必须记载了请求配置信息
WHICHE_LIST = 1  # 指定哪一个产品列表 1.todo_ 待发布 2.offline 下架 3.online 在线  5. 测试用
OP_CODE_STATE = 1  # 1保存 2发布
FILTER_STATE = 1  # 上货过滤控制  0全不过滤直接干 1过滤已经编辑好的

# if __name__ == '__main__':
#     print(_shao_kang["sku_template_file"])
