# zip(*iterables)
# 接收多个可迭代对象（字符串、列表、元组等）
# 按位置配对元素，生成一个个元组
# 长度以最短的序列为准，多余元素直接舍弃
a = [1,2,3]
b = ['x','y','z']
res = zip(a, b)
res1 = (a,b)

print(list(res))
# [(1, 'x'), (2, 'y'), (3, 'z')]

# 组包
print(list(res1))
# [[1, 2, 3], ['x', 'y', 'z']]
print(res1)
# ([1, 2, 3], ['x', 'y', 'z'])

# 解包
for c, n in zip(a, b):
    print(c,n)



# 案例
def romanToInt(s: str) -> int:
    res = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for char, n in zip(s, s[1:]):
        if roman[char] < roman[n]:
            res -= roman[char]
        else:
            res += roman[char]
    res += roman[s[-1]]
    return res
