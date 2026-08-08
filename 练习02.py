# 给你一个字符串 s，找到 s 中最长的 回文 子串。
def longestPalindrome(self, s: str) -> str:
    # 中心扩散法
    def expend(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    res = ""
    for i in range(len(s)):
        # 奇数回文串
        odd = expend(i, i)
        # 偶数回文串
        even = expend(i, i + 1)
        if len(odd) > len(res):
            res = odd
        if len(even) > len(res):
            res = even
    return res
