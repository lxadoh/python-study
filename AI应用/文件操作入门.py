# 文件操作入门
# # 读取文件
# # 1. 打开文件
# # with 语句不论是否发生异常,自动关闭文件，无需手动关闭,推荐使用，不用调用close()
# with open("resources/社会热点.txt", "r", encoding="utf-8") as f:
#     # 2. 读取文件内容
#
#     # # 读取文件所有内容
#     # content = f.read()
#     # print(content)
#
#     # 按行读取
#     # lines = f.readlines()
#     # for line in lines:
#     #     # strip() 方法用于移除字符串头尾指定的字符（默认为空格、换行符）
#     #     print(line.strip())


# 写入文件

"""
路径写法：
    1. 绝对路径：从根目录开始的完整路径
        例如：D:\\pycharmdm\\pystudy\\AI应用\\resources\\静夜思.txt
        注意：Windows系统中，路径中的反斜杠需要使用双反斜杠或正斜杠替换
        例如：D:/pycharmdm/pystudy/AI应用/resources/静夜思.txt

    2. 相对路径：从当前文件所在目录开始的路径
        . ：表示当前目录----> ./resources/静夜思.txt
        .. ：表示上一级目录----> ../AI应用/resources/静夜思.txt
"""

# 1. 打开文件
# 相对路径：从当前文件所在目录开始的路径
with open("./resources/静夜思.txt", "w", encoding="utf-8") as f:
    # 2. 写入文件内容
    f.write("床前明月光，疑是地上霜。\n"
            "举头望明月，低头思故乡。")


# # 追加文件(作用：在文件末尾追加内容，不会覆盖原文件内容)
# # 1. 打开文件
# with open("resources/静夜思.txt", "a", encoding="utf-8") as f:
#     # 2. 写入文件内容
#     f.write("\n"
#             "床前明月光，疑是地上霜。\n"
#             "举头望明月，低头思故乡。")
