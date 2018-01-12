# -*- coding: utf-8 -*-
#给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)
#代码未能通过测试....return:nothing
class Solution:
    """
    @param: str: An array of char
    @param: offset: An integer
    @return: nothing
    """
    def rotateString(self, strs, offset):
        # write your code here
        liststr = []
        i = offset
        while i > 0:
            liststr.append(strs[-i])
            i = i - 1
        i = 0
        while i < len(strs) - offset:
            liststr.append(strs[i])
            i = i + 1
        return ''.join(liststr)
            
s1 = Solution()
strs = "abcdefg"
s1.rotateString(strs,3) 