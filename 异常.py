# 异常
# try:
#     print("-----------")
#     # print(my_name)
#     # print(1 / 0)
#     print("abc"[3])
#     print("-----------")
# # except NameError as e:
# #     print("程序出错了，请联系管理员：异常信息：", e)
# # except ZeroDivisionError as e:
# #     print("程序出错了，请联系管理员：异常信息：", e)
# # except IndexError as e:
# #     print("程序出错了，请联系管理员：异常信息：", e)
# except Exception as e:   # 可以捕获所有异常
#     print("程序出错了，请联系管理员：异常信息：", e)
# finally:   # 无论程序是否正常运行，都会运行
#     print("+++++++++")
#

# # 异常的传递
# def fun1():
#     print("fun1...running...")
#     fun2()
#
#
# def fun2():
#     print("fun2...running...")
#     fun3()
#
#
# def fun3():
#     print("fun3...running...")
#     print(my_color)
#
#
# if __name__ == "__main__":
#     try:
#         fun1()
#     except Exception as e:
#         print("程序出错了，请联系管理员：异常信息：", e)