# 封装 : 将属性和方法封装到类中，只暴露必要的接口
# 私有属性和方法 : 用下划线开头的属性和方法，只能在类内部调用
# 公有属性和方法 : 用下划线开头的属性和方法，可以在类外部调用


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



if __name__ == "__main__":
    car = Car("奔驰", "红色", "S级", "张三")
    print(car.brand)
    print(car.color)
    print(car.model)
#    print(car.__owner) 调用私有属性(错误)

    car.start()
    car.run()
    car.stop()
#    car.__control_fuel() 调用私有方法(错误)
    print(car.get_owner())
