# # 函数定义
# def out_line():
#     print("-------------------------")
#
# # 函数调用
# out_line()
#
#
# # 函数的参数与返回值
# # 函数1：计算圆的面积
# def circle_area(r):
#     """
#     根据圆的半径，计算圆的面积
#     :param r: 圆的半径
#     :return: 圆的面积
#     """
#     area = 3.14 * r * r
#     return area
#
# print(circle_area(10))
#
#
# # 函数2：计算长方形的面积
# def rectangle_area(l, w):
#     """
#     根据长方形的长和宽，计算长方形的面积
#     :param l: 长方形的长
#     :param w: 长方形的宽
#     :return: 长方形的面积
#     """
#     area = l * w
#     return area
#
# print(rectangle_area(2, 7))
#
#
# # 函数3：计算圆的面积和周长(多返回值，逗号隔开)
# def circle_area_len(r):
#     """
#     根据圆的半径，计算圆的面积和周长
#     :param r: 圆的半径
#     :return:圆的面积和周长
#     """
#     return 3.14 * r * r, round(2 * 3.14 * r, 1)  #round() 保留小数
#
# area, len = circle_area_len(5)
# print(f"面积：{area}, 周长：{len}")
#
#

# 案例
# 定义一个函数：计算传入班级学生高考成绩列表中的最高分，最低分，平均分（保留一位小数）
def score_max_min_avg(score_list):
    """
    根据班级学生高考成绩列表，计算得到最高分，最低分，平均分
    :param score_list: 班级学生高考成绩列表
    :return: 最高分，最低分，平均分
    """
    score_max = max(score_list)
    score_min = min(score_list)
    score_avg = round(sum(score_list) / len(score_list), 1)
    return score_max, score_min, score_avg

list1 = [654, 546, 578, 598, 643, 456, 576, 655]
score_max, score_min, score_avg = score_max_min_avg(list1)
print(f"最高分：{score_max}，最低分：{score_min}，平均分：{score_avg}")