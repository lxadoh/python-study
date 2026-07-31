# # 列表
# # 定义列表
# s = [3, 4, 2, 1, 5, 'a', 'hello', True]

# # 列表操作
# # 获取
# print(s[0])   # 正向索引从0开始
# print(s[-8])  # 反向索引从-1开始
#
# # 修改,不能超出索引范围
# s[5] = 'abc'
# print(s)
#
# # 删除
# del s[5]
# print(s)
#
# # 遍历
# for item in s:
#     print(item)

# # 列表切片  s[开始索引：结束索引：步长]
# print(s[0:5:1])
# print(s[:5:])
# print(s[:5])
# print(s[0:5:2])
# print(s[0:-2:1])
# print(s[::-1])   # 反向打印

# # 列表方法
# # append() 在列表尾部追加元素
# s.append(188)
# print(s)
#
# # insert() 在指定索引前插入元素
# s.insert(2,45)
# print(s)
#
# # remove() 移除第一个匹配到的元素
# s.remove(45)
# print(s)
#
# # pop() 弹出并返回指定索引位置的元素，默认弹出最后一个
# a = s.pop(1)
# print(s)
#
# # sort() 排序，元素类型需一致,默认正向
# s1=[2,4,6,4,3,1,5,7,1]
# s1.sort()
# print(s1)
#
# # reverse() 反转列表
# s.reverse()
# print(s)


# # 合并两个列表并去重
# num_list1 = [1, 5, 3, 1, 9, 8, 6, 4]
# num_list2 = [34, 756, 23, 2, 3, 1, 6, 7, 443]
#
# # for i in num_list2:    # 遍历直接合并，不推荐
# #     num_list1.append(i)
#
# # # 解包：将列表这一类数据容器解开成一个一个元素
# # num_list = [*num_list1, *num_list2]
#
# # 直接相加
# num_list = num_list1 + num_list2
#
# print(num_list)
# s = set(num_list)
# print(s)
# new_list = list(s)
# print(new_list)

# # 生成1到20的平方列表
# num_list1 = list(i**2 for i in range(1,21))
# print(num_list1)
#
# # 生成1到20的偶数平方列表
# num_list2 = list(i**2 for i in range(1,21) if i % 2 == 0)
# print(num_list2)