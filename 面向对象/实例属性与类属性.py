# 定义类
class Car:
    # 类属性(所有实例对象共享)
    wheel = 4   # 轮胎数量
    tax_rate = 0.1   # 购置税税率

    # __init__：是初始化的方法，会在对象创建时自动调用，可以为对象设置对应的属性
    # self：是第一个参数，表示当前所创造出来的实例对象
    def __init__(self,c_color, c_brand, c_name, c_price):
        # 实例属性(访问会先查找实例属性，再查找类属性)
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price

    # 实例方法
    def running(self):
        print(f"{self.brand} {self.name}正在高速行驶中...")

    def total_cost(self, discount, rate):
        """
        计算提车的总费用，包含车的价格和税
        :param discount: 折扣
        :param rate: 税率
        :return: 提车的总价格
        """
        return self.price * discount + self.price * rate

    # 魔法方法(在合适时机自动调用) __init__也是
    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price}"

    def __eq__(self, other):
        return self.color == self.color and self.price == self.price and self.name == self.name and self.brand == self.brand

    def __lt__(self, other):
        return self.price < other.price



# 测试
c1 = Car("红色", "BMW", "X7", 800000)
c2 = Car("黑色", "Tesla", "R6", 700000)

# 通过类名调用类属性
print(Car.wheel)
s = []
s.append(c1)
s.append(c2)
print(s[1])