# 导入模块
# import utils.out_name
#
#
# print(utils.out_name.NAME)

# from utils import out_name
#
#
# print(out_name.NAME)

# # 要通过from utils import *导入包下的所有模块，要在__init__.py文件里添加__all__ = []
# from utils import *
# print(out_name.NAME)


# 导入模块中的功能
# utils.out_name会从当前文件查找
# from utils.out_name import NAME
# 绝对路径module.utils.out_name
from module.utils.out_name import NAME
print(NAME)