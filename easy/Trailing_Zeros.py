# -*- coding: utf-8 -*-
#设计一个算法，计算出n阶乘中尾部零的个数
#O(logN)的时间复杂度
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        zeronum = 0
        while n >= 5:
            zeronum = zeronum + int(n / 5)
            n = int(n / 5)
        return zeronum


s1 = Solution()
print(s1.trailingZeros(101))