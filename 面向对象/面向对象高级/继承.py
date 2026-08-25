# 继承 : 子类可以继承父类的属性和方法(私有属性和方法不能继承)
# 重写 : 子类可以重写父类的方法(方法名相同，参数相同)
# 重载 : 子类可以重载父类的方法(方法名相同，参数不同)

# 车类
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

# 华为AI驾驶类
class HuaweiAiDriving:
    def __init__(self, version="V1.0"):
        self.version = version # 版本

    def run(self):
        print(f"正在使用华为AI驾驶系统{self.version}行驶...")


# 燃油车 : 继承自车类
class FuelCar(Car):
    # 加油(重写父类方法)
    def charge(self):
        # 调用父类方法
        # 法一
        super().charge()

        # # 法二
        # Car.charge(self)

        print(f"{self.brand}{self.model} 正在加油...")

    # 补充燃料(重载父类方法)
    def charge(self, fuel_type="汽油"):
        # # 调用父类方法
        # super().charge()
        print(f"{self.brand}{self.model} 正在补充{fuel_type}...")


# 电车 : 继承自车类
class ElectricCar(Car):
    def charge(self):
        super().charge() # 调用父类方法
        print(f"{self.brand}{self.model} 正在充电...")


# 问界汽车 : 继承自车类和华为AI驾驶类(多继承)
class WenJieCar(Car, HuaweiAiDriving):
    # 初始化方法
    def __init__(self, brand, color, model, owner, version="V1.0"):
        Car.__init__(self, brand, color, model, owner)
        HuaweiAiDriving.__init__(self, version)

    def run(self):
        Car.run(self)
        HuaweiAiDriving.run(self)

if __name__ == "__main__":
    # 重写父类方法
    # fuel_car = FuelCar("奔驰", "红色", "S级", "张三")
    # fuel_car.charge()
    # """
    # 输出 :
    # 奔驰S级 正在补充燃料...
    # 奔驰S级 正在加油...
    # """


    # 多继承
    # MRO : 方法解析顺序：左到右，从上到
    # print(WenJieCar.__mro__)
    # print(WenJieCar.mro())
    c = WenJieCar("奔驰", "红色", "S级", "张三")
    # __dict__：是对象的一个属性，会将对象中的所有属性以字典的形式输出
    print(c.__dict__)
    c.run()