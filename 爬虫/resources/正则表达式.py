import re

s1 = "18809090000是我的手机号，你记住了吗？ 我的帘，机学是18800008888，两个QQ号分别是155998992 和 18809091293821 你记住了吗？"
s2 = "我的手机号是18809090000，你记住了吗？ 我的第一个手机号是18300608888。两个QQ号分别是155998992和 18809091293821 你记住了吗？"

# match 方法：从字符串开头开始匹配，(匹配第一个匹配项)
# r 表示原始字符串，避免转义字符
# 1[3-9]\d{9} 表示以1开头，后面跟着3-9之间的数字，后面跟着9个数字
# result = re.match(r"1[3-9]\d{9}", s2) 结果是 None
result = re.match(r"1[3-9]\d{9}", s1)
print(result) # <re.Match object; span=(0, 11), match='18809090000'>
print(result.group()) # group() ：返回匹配的字符串 18809090000
print(result.span()) # span() ：返回匹配的字符串的索引范围 (0, 11)
print(result.start()) # start() ：返回匹配的字符串的起始索引 0
print(result.end()) # end() ：返回匹配的字符串的结束索引 11

# search 方法：从字符串任意位置开始匹配，搜索第一个匹配项
result = re.search(r"1[3-9]\d{9}", s2)
print(result) # <re.Match object; span=(6, 17), match='18809090000'>
print(result.group()) # group() ：返回匹配的字符串 18809090000
print(result.span()) # span() ：返回匹配的字符串的索引范围 (6, 17)
print(result.start()) # start() ：返回匹配的字符串的起始索引 6
print(result.end()) # end() ：返回匹配的字符串的结束索引 17

# findall 方法：从字符串任意位置开始匹配，返回所有匹配项的列表 -> list
result = re.findall(r"1[3-9]\d{9}", s2)
print(result) # ['18809090000', '18300608888']
print(result[0]) # 18809090000
print(result[1]) # 18300608888

# 语法*， ^， $, \d， \D， \s， \S， \w， \W, ., ?, +, *, |, (, ), [ ], { }, \
# * 表示任意次数，+ 表示至少一次，? 表示可选一次 (只要满足，就会一直匹配)贪婪匹配
# {m,n} 表示 m 到 n 次
# [fafad] 表示 f、a、f、a、d 中的任意一个字符
# [^fafad] 表示 除了 f、a、f、a、d 以外的任意一个字符
# () 表示捕获组，| 表示或
# ^ 表示字符串开头，$ 表示字符串结尾
# \d 表示数字，\D 表示非数字
# \s 表示空格，\S 表示非空格
# \w 表示字母数字下划线，\W 表示非字母数字下划线
# . 表示任意字符，\n 表示换行符