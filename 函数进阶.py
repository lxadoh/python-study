# 函数
# # 全局变量，局部变量
# num1 = 1  # 全局变量
# def fun1():
#     num1 = 100  # 局部变量
#     print(num1)
#
# fun1()
# print(num1)
#
#
# num2 = 1
# def fun2():
#     global num2  # 声明函数使用全局变量num2
#     num2 = 100
#     print(num2)
#
# fun2()
# print(num2)


# 参数
# # 定义函数
# def reg_stu(name, age, gender, city):
#     print("注册成功")
#     return {"name": name, "age": age, "gender": gender, "city":city}
#
# # 位置参数
# reg_stu("张三", 18, "男", "北京")
#
# # 关键字参数(无位置要求，可无序)
# reg_stu(name="李四", age=20, gender="男", city="武汉")
#
# # 位置参数+关键字参数(关键字参数要在位置参数后面)
# reg_stu("张三", 18, gender="男", city="武汉")
#
#
# # 默认参数(默认参数要放在其他参数后面)
# def reg_stu1(name, age, gender, city="北京"):
#     print("注册成功")
#     return {"name": name, "age": age, "gender": gender, "city":city}
#
# reg_stu1("小米", 24, "男")
# # 如果与默认参数不一致，可以自己修改
# reg_stu1("小米", 24, "男", "上海")


# # 不定长参数
# # 不定长参数-位置参数(*)：这些参数会在封装在元组中 *args -> 元组tuple
# def calc_data(*args):
#     data_min = max(args)
#     data_max = min(args)
#     data_avg = round(sum(args) / len(args), 1)
#     return data_min, data_max, data_avg
#
# # 函数调用
# print(calc_data(2, 3, 5, 4, 6, 4, 33, 54))
# print(calc_data(2, 3, 5, 4, 1, 54, 33, 67, 32, 21))
#
#
# # 不定长参数-关键字参数:(**) **kwargs -> 字典dict
# def calc_data1(*args, **kwargs):
#     data_min = max(args)
#     data_max = min(args)
#     data_avg = sum(args) / len(args)
#     if kwargs.get("round") is not None:
#         data_avg = round(data_avg, kwargs.get("round"))
#     return data_min, data_max, data_avg
#
#
# print(calc_data1(2, 3, 5, 4, 6, 4, 33, 54, round=2))
#

# # 参数类型
# # 普通参数：数字，布尔，字符串，列表，元组，集合。字典
#
#
# # 特殊参数：函数
# # 加
# def add(x, y):
#     return x+y
#
# # 减
# def substract(x, y):
#     return x-y
#
# # 乘
# def multiply(x, y):
#     return x*y
#
# # 除
# def divide(x, y):
#     return x/y
#
# # 计算
# def calc(x, y, oper):
#     return oper(x, y)
#
# # 函数调用
# print(calc(10, 5, add))


# 匿名函数：函数逻辑简单，且只在一个地方使用(返回结果时，不需要写return，表达式运算结果就是返回结果)
out_line = lambda : print("-----------------")
out_line()

add = lambda x, y : x+y
print(add(10, 5))


# 函数注解
# 函数3：计算圆的面积和周长(多返回值，逗号隔开)
def circle_area_len(r: float) -> tuple[float, float]:
    """
    根据圆的半径，计算圆的面积和周长
    :param r: 圆的半径
    :return:圆的面积和周长
    """
    return 3.14 * r * r, round(2 * 3.14 * r, 1)  #round() 保留小数

area, len = circle_area_len(5.0)
print(f"面积：{area}, 周长：{len}")
