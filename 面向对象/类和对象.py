# # 定义类(类名：每个单词都要大写且没有分隔符)
# class Car:
#     pass
#
#
# # 创建对象
# c1 = Car()
# # 动态为对象添加属性(不推荐)
# c1.color = "red"
# c1.price = 500000
# c1.name = "X5"
# c1.brand = "BMW"
#
# print(c1)   # 输出的是对象的存储地址
# print(c1.brand)   # "BMW"
# print(c1.__dict__)   # 会将对象中的所有属性以字典的形式输出


# 定义类
class Car:
    # __init__：是初始化的方法，会在对象创建时自动调用，可以为对象设置对应的属性
    # self：是第一个参数，表示当前所创造出来的实例对象
    def __init__(self,c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car类的对象初始化完成，对象属性已添加。")


# 参数要完整
c1 = Car("红色", "BMW", "X7", 800000)
# __dict__：是对象的一个属性，会将对象中的所有属性以字典的形式输出
print(c1.__dict__)