# 请你来实现一个 myatoi(s) 函数，使其能将字符串转换成一个 32 位有符号整数。
#
# 函数 myatoi(s) 的算法如下：
#
# 空格：读入字符串并丢弃无用的前导空格（" "）
# 符号：检查下一个字符（假设还未到字符末尾）为 '-' 还是 '+'。如果两者都不存在，则假定结果为正。
# 转换：通过跳过前置零来读取该整数，直到遇到非数字字符或到达字符串的结尾。如果没有读取数字，则结果为0。
# 舍入：如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。
# 具体来说，小于 −231 的整数应该被舍入为 −231 ，大于 231 − 1 的整数应该被舍入为 231 − 1 。
# 返回整数作为最终结果。


def myatoi(s: str) -> int:
    n = len(s)
    i = 0
    while i < n and s[i] == " ":
        i += 1
    sign = 1  # 符号位
    if i < n and s[i] in "-+":
        sign = 1 if s[i] == "+" else -1
        i += 1
    res = 0
    mx = (1 << 31) - 1  # 32位最大值
    while i < n and s[i].isdigit():
        digit = ord(s[i]) - ord('0')  # ASCII 差值手动计算
        res = res * 10 + digit
        if res > mx:
            return mx if sign == 1 else -(1 << 31)
        i += 1
    return res * sign


# 测试
print(myatoi(" 345fsf"))
print(myatoi(" -sfd4"))
print(myatoi("    -24"))
print(myatoi(" -+45"))
print(myatoi("1-1"))