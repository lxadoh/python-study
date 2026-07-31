# 元组
# # 元组方法
# t1 = (42, 4, 321, 67, 54, 3, 2, 1, 7, 4)
# # count() 统计元素出现次数
# print(t1.count(4))
#
# # index() 查找元素第一次出现的索引位置
# print(t1.index(3))
#
# # 如果要定义单元素元组，要加逗号
# t2 = (100,)
# print(type(t2))
# t3 = (100)
# print(type(t3))

# # 组包与解包
# # 组包
# t1 = (5, 43, 2, 65)
# t2 = 3, 4, 2, 6
# print(t1)
# print(t2)
#
# # 解包,元素个数要统一
# a, b, c, d = t1
# print(a, b, c, d)
#
# a, *b, c = t2
# print(a, b, c)
#
# *a, b = t2
# print(a, b)


# # 案例
# # 交换数值
# a = 10
# b = 20
#
# # # 组包
# # t = b, a
# #
# # # 解包
# # a, b = t
#
# # 合并简写
# a, b = b, a
#
# print(a,b)


