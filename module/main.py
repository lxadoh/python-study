# # 导入自定义模块
# import my_fun
#
# # 使用模块中的功能
# print(my_fun.PI)
# print(my_fun.NAME)
#
# my_fun.out_line1()
# my_fun.out_line3()


# 导入自定义模块中的功能
# from my_fun import PI, NAME, out_line1, out_line3
from my_fun import *

# 使用模块中的功能
print(PI)
print(NAME)

out_line1()
out_line3()
# out_line4()   报错
