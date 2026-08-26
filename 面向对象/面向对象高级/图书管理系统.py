from abc import ABC, abstractmethod
import json

# 书籍类
class Book:
    def __init__(self, book_id, title, author, total_num):
        self.book_id = book_id # 书籍编号
        self.title = title # 书籍标题
        self.author = author # 作者
        self.total_num = total_num # 总数量
        self.__available_num = total_num # 可借数量


    # 借阅书籍
    def borrow_book(self):
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        return False

    # 归还书籍
    def return_book(self):
        self.__available_num += 1

    # 获取可借数量
    def get_available_num(self):
        return self.__available_num


# 抽象类： 是一个不能直接实例化的类，只能被继承，它定义了一组方法，这些方法在子类中必须实现，但是具体实现由子类来决定
# python中的抽象类： 抽象类的定义需要使用abc模块中的ABC类: 抽象类的基类 和 abstractmethod装饰器
# 会员类 ： 抽象类
class Member(ABC):
    def __init__(self, member_id, name, password):
        self.member_id = member_id # 会员编号
        self.name = name # 会员姓名
        self.__password = password # 密码
        self.__borrowed_books = [] # 已借书籍列表


    # 抽象方法： 必须在子类中实现，但是具体实现由子类来决定
    # 获取最大借阅数量
    @abstractmethod
    def get_max_book(self) -> int:
        pass


    # 借阅书籍
    def borrow_book(self, book: Book):
        # 判断当前会员借阅数量是否达到最大限制
        if len(self.__borrowed_books) >= self.get_max_book():
            print("当前会员已借阅数量已达最大限制")
            return False

        # 判断书籍是否可借
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name} 已借阅 {book.title}")
            return True
        else:
            print(f"借阅失败，{book.title} 已被借完")
            return False


    # 归还书籍
    def return_book(self, book: Book):
        # 判断书籍是否在已借书籍列表中
        if book not in self.__borrowed_books:
            print(f"归还失败，{self.name} 未借阅 {book.title}")
            return False
        else:
            self.__borrowed_books.remove(book)
            book.return_book()
            print(f"{self.name} 已归还 {book.title}")
            return True


    # 获取密码
    def get_password(self):
        return self.__password


    # 获取已借书籍列表
    def get_borrowed_books(self):
        return self.__borrowed_books


# 普通会员类
class NormalMember(Member):
    # 获取最大借阅数量(普通会员)
    def get_max_book(self) -> int:
        return 3

# Vip会员类
class VipMember(Member):
    def __init__(self, member_id, name, password, vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level # Vip等级

    # 获取最大借阅数量(Vip会员)
    def get_max_book(self) -> int:
        return 6 + self.vip_level


# 图书管理系统类
class LibrarySystem:
    def __init__(self):
        self.books = {} # 书籍列表 键：书籍编号 值：Book对象
        self.members = {} # 会员列表 键：会员编号 值：Member对象
        self.current_member: Member|None = None # 当前登录会员
        # 加载书籍和会员数据
        self.load_books()
        self.load_members()


    # 加载书籍数据
    def load_books(self):
        # 加载data/books.js文件中的书籍数据
        with open("data/books.json", "r", encoding="utf-8") as f:
            book_data = json.load(f)
            for book in book_data:
                self.books[book["编号"]] = Book(book["编号"], book["标题"], book["作者"], book["数量"])
            print("加载书籍数据成功！")


    # 加载会员数据
    def load_members(self):
        # 加载data/members.js文件中的会员数据
        with open("data/members.json", "r", encoding="utf-8") as f:
            member_data = json.load(f)
            for member in member_data:
                if member["卡号"].startswith("N"):
                    self.members[member["卡号"]] = NormalMember(member["卡号"], member["姓名"], member["密码"])
                elif member["卡号"].startswith("V"):
                    self.members[member["卡号"]] = VipMember(member["卡号"], member["姓名"], member["密码"], int(member["会员等级"]))
            print("加载会员数据成功！")


    # 登录
    def login(self):
        while True:
            print("\n【登录】")

            member_id = input("请输入会员编号：")
            # 判断会员是否存在
            if member_id not in self.members:
                print("登录失败，会员不存在")
                continue

            password = input("请输入会员密码：")
            # 判断密码是否正确
            member = self.members[member_id]
            if member.get_password() == password:
                print(f"登录成功,欢迎 {member.name}")
                self.current_member = member
                return True
            else:
                print("登录失败，密码错误!")
                continue


    # 借阅图书
    def borrow_book(self):
        # 1.展示所有书籍
        for book in self.books.values():
            print(f"编号：{book.book_id} 标题：{book.title} 作者：{book.author} 总数：{book.total_num} 可借：{book.get_available_num()}")

        # 2.获取用户输入的书籍编号，执行借阅操作
        book_id = input("请输入要借阅的书籍编号：")
        if book_id not in self.books:
            print("借阅失败，书籍不存在")
            return
        self.current_member.borrow_book(self.books[book_id])


    # 归还图书
    def return_book(self):
        borrowed_books = self.current_member.get_borrowed_books()
        # 判断会员是否有已借书籍
        if len(borrowed_books) == 0:
            print("您没有借阅任何书籍！")
            return
        else:
            # 1.展示所有已借书籍
            print("【已借书籍】")
            for book in borrowed_books:
                print(f"编号：{book.book_id} 标题：{book.title} 作者：{book.author}")

            # 2.获取用户输入的书籍编号，执行归还操作
            book_id = input("请输入要归还的书籍编号：")
            if book_id not in self.books:
                print("归还失败，书籍不存在")
                return
            self.current_member.return_book(self.books[book_id])


    # 查看借阅记录
    def show_borrowed_books(self):
        # 1.展示所有已借书籍
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) > 0:
            print("【已借书籍】")
            for book in borrowed_books:
                print(f"编号：{book.book_id} 标题：{book.title} 作者：{book.author}")
        else:
            print("您没有借阅任何书籍！")


    # 运行
    def run(self):
        if self.login():
            while True:
                print("\n1. 借阅图书")
                print("2. 归还图书")
                print("3. 查看借阅")
                print("4. 退出系统")

                choice = input("请选择操作(1-4)：")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_borrowed_books()
                    case "4":
                        break
                    case _:
                        print("无效选择，请重新选择！")


if __name__ == "__main__":
    library = LibrarySystem()
    library.run()
