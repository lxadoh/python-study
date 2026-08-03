# __all__；用于指定from 模块名 import *时会导入哪些功能
__all__ = ["PI", "NAME", "out_line1", "out_line3"]

# 常量(大写，不会发生变化的数据)
PI = 3.1415926
NAME = "lxadoh"


# 函数
def out_line1():
    print("-" * 30)


def out_line2():
    print("+" * 30)


def out_line3():
    print("#" * 30)


def out_line4():
    print("*" * 30)


# 测试函数
# __name__ ：内置变量，表示当前模块的名字(直接运行模块是，__name__值为__main__；当前模块被导入时，值就是当前模块的名字)
# 则执行当前文件时，才会执行测试函数；如果被当作模块导入，就不会执行
if __name__ == "__main__":
    out_line1()
