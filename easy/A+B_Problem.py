# -*- coding: utf-8 -*-
class Solution:
    """
    @param: a: An integer
    @param: b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        
        if a == -b:
            return 0
        # write your code here
        add = a ^ b
        carry = (a & b) << 1
        while carry != 0:
            add = a ^ b
            carry = (a & b) << 1
            a = add
            b = carry
        return add
    
s1 = Solution()
print(s1.aplusb(100,4))