#  集合
# 集合方法
s1 = {1, 2, 3, 4, 34, 5, 21, 65}
# add() 添加元素
s1.add(100)
print(s1)

# remove() 移除指定元素，不存在则报错
s1.remove(1)
print(s1)

# pop() 随机删除元素并返回
e = s1.pop()
print(e)
print(s1)

# clear() 清空集合
s1.clear()
print(s1)

s2 = {9, 7, 5, 4, 2, 8, 1, 3}
s3 = {1, 6, 4, 3, 8}
# difference() 求两个集合的差集
print(s2.difference(s3))

# union() 求并集
print(s2.union(s3))

# intersection() 求交集
print(s2.intersection(s3))
