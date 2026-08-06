class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

    def __str__(self):
        return f"姓名：{self.name} 语文：{self.chinese} 数学：{self.math} 英语：{self.english}"


class StudentManagement:
    def __init__(self):
        self.stu_list = []

    # 添加学生
    def add_stu(self):
        name = input("请输入学生姓名：")

        for s in self.stu_list:   #判断学生是否在系统中
            if s.name == name:
                print("该学生已存在。")
                return

        while True:
            chinese = float(input("请输入学生语文成绩："))
            math = float(input("请输入学生数学成绩："))
            english = float(input("请输入学生英语成绩："))

            if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                break
            else:
                print("成绩范围要在0-100之间！")

        self.stu_list.append(Student(name, chinese, math, english))
        print("学生添加成功。")


    def update_stu(self):
        name = input("请输入学生姓名：")

        for s in self.stu_list:  # 判断学生是否在系统中
            if s.name == name:
                print(f"修改前成绩：{s}")
                chinese = s.chinese
                math = s.math
                english = s.english

                while True:
                    stu_chinese = input("请输入学生修改后语文成绩：")
                    if stu_chinese != "":
                        chinese = float(stu_chinese)
                        if chinese < 0 or chinese > 100:
                            print("成绩范围要在0-100之间！")
                            continue

                    stu_math = input("请输入学生修改后数学成绩：")
                    if stu_math != "":
                        math = float(stu_math)
                        if math < 0 or math > 100:
                            print("成绩范围要在0-100之间！")
                            continue

                    stu_english = input("请输入学生修改后英语成绩：")
                    if stu_english != "":
                        english = float(stu_english)
                        if english < 0 or english > 100:
                            print("成绩范围要在0-100之间！")
                            continue
                    break

                s.update_score(chinese = chinese, math = math, english = english)
                print("成绩修改成功。")
                print(f"修改后成绩：{s}")
                return

        print("该学生不存在！")


    def delete_stu(self):
        name = input("请输入学生姓名：")

        for s in self.stu_list:  # 判断学生是否在系统中
            if s.name == name:
                self.stu_list.remove(s)
                print("学生信息删除成功。")
                return
        print("该学生不存在！")


    def search_stu(self):
        name = input("请输入学生姓名：")

        for s in self.stu_list:  # 判断学生是否在系统中
            if s.name == name:
                print(s)
                return
        print("该学生不存在！")


    def show_all_stu(self):
        for s in self.stu_list:
            print(s)

    def menu_stu(self):
        while True:
            print("""
            ----------------
            - 1.添加学生信息 -
            - 2.修改学生信息 -
            - 3.删除学生信息 -
            - 4.查询学生信息 -
            - 5.展示学生信息 -
            - 6.退出学生系统 -
            ----------------
            """)
            choice = input("请输入操作序号：")
            try:
                match choice :
                    case "1":
                        self.add_stu()
                    case "2":
                        self.update_stu()
                    case "3":
                        self.delete_stu()
                    case "4":
                        self.search_stu()
                    case "5":
                        self.show_all_stu()
                    case "6":
                        break
                    case _ :
                        print("非法序号，请重新输入：")
            except ValueError:
                print("输入的数据有问题，请重新输入！")
            except Exception:
                print("程序运行错误，请重新操作！")


if __name__ == "__main__":
    stu_management = StudentManagement()
    stu_management.menu_stu()