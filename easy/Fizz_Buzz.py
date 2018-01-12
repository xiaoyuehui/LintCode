# -*- coding: utf-8 -*-
'''
给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：

如果这个数被3整除，打印fizz.
如果这个数被5整除，打印buzz.
如果这个数能同时被3和5整除，打印fizz buzz.
'''

class Solution:
    """
    @param: n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        liststr = []
        for i in range(n + 1):
            if i == 0:
                continue
            if i % 15 == 0:
                liststr.append('fizz buzz')
                continue
            if i % 3 == 0:
                liststr.append('fizz')
                continue
            if i % 5 == 0:
                liststr.append('buzz')
                continue
            liststr.append(str(i))
        return liststr
            
s1 = Solution()
l = s1.fizzBuzz(15)
print(l)
            
                