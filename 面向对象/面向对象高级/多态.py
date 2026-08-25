# 多态 : 不同对象对同一方法的响应不同


# Car类
class Car:
    def __init__(self, brand, color, model, owner):
        self.brand = brand # 品牌
        self.color = color # 颜色
        self.model = model # 型号
        self.__owner = owner # 所有者(私有属性)

    def start(self): # 启动
        print(f"{self.brand}{self.model} 正在启动...")

    def run(self): # 行驶
        print(f"{self.brand}{self.model} 正在行驶...")
        self.__control_fuel() # 控制燃油(私有方法)

    def stop(self): # 停止
        print(f"{self.brand}{self.model} 正在停止...")

    def __control_fuel(self): # 控制燃油(私有方法)
        print(f"{self.brand}{self.model} 正在控制燃油...")

    def get_owner(self): # 获取所有者(公有方法)
        return self.__owner[0] + "**"

    def charge(self):
        print(f"{self.brand}{self.model} 正在补充燃料...")


# 燃油车 : 继承自车类
class FuelCar(Car):
    def charge(self):
        print(f"{self.brand}{self.model} 正在加油...")


# 电车 : 继承自车类
class ElectricCar(Car):
    def charge(self):
        print(f"{self.brand}{self.model} 正在充电...")


# 补充燃料 : 多态调用
def handle_charge(car: Car): # 函数参数声明 : 车类的实例
    car.charge()


# 测试
if __name__ == "__main__":
    handle_charge(FuelCar("奔驰", "红色", "S级", "张三"))
    handle_charge(ElectricCar("特斯拉", "白色", "Model S", "李四"))
