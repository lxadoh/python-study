# 字符串
# # 常用方法
# s = "hello world"
# # find() 查找子串，返回第一次出现的索引，找不到返回-1
# index = s.find('o')
# print(index)
#
# # count() 统计子串在字符串出现的次数
# print(s.count('l'))
#
# # upper() 大写    lower() 小写
# print(s.upper())
# print(s.lower())
#
# # split() 将字符串按照指定分隔符分割成列表
# print(s.split(" "))
#
# # strip() 去除字符串两端空白字符或指定字符
# a=' sfl '
# print(a.strip())
#
# # replace() 将指定子串转换成新的子串
# print(s.replace(' ', ','))
#
# # startswith() 检查字符串是否以指定子串开头，返回布尔值
# print(s.startswith('hello'))
#
# # 字符串不可变
# print(s)

# # 用户输入10个字符串,反转并大写，然后记录在列表中，并遍历输出
# num = []
# list1 = input("请输入10个字符串，以空格分开:").split(" ")
# for i in list1:
#     s = i.upper()
#     num.append(s[::-1])
# for j in num:
#     print(j)


# # 输入字符串，判断是否是回文
# s = input("请输入字符串：")
# # # 法1
# # if s == s[::-1]:
# #     print(f"{s}是回文")
# # else:
# #     print(f"{s}不是回文")
#
# # # 法2：双指针法
# # left = 0
# # right = len(s)-1
# # flag = True
# # while left < right:
# #     if s[left] != s[right]:
# #         flag = False
# #         break
# #     left += 1
# #     right -= 1
# # if flag:
# #     print(f"{s}是回文")
# # else:
# #     print(f"{s}不是回文")
