
# 鸭子类型 : 不强制要求类实现某个接口，而是根据类的行为来判断是否符合要求
# 不关注对象的类型，只关注对象的行为是否符合要求
# 例如 : 鸭子、狗、猪都可以游泳

class Duck:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"{self.age}岁的{self.name} 正在游泳...")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"{self.age}岁的{self.name} 正在游泳...")


class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"{self.age}岁的{self.name} 正在游泳...")


def go_swimming(duck):
    duck.swimming()


# 测试
if __name__ == "__main__":
    go_swimming(Duck("鸭子", 1))
    go_swimming(Dog("狗", 2))
    go_swimming(Pig("猪", 3))
