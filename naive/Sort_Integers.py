# -*- coding: utf-8 -*-
class Solution:
    """
    @param: A: an integer array
    @return: 
    """
    def sortIntegers(self, A):
        # write your code here
        for i in range(len(A) -1):
            for j in range(len(A) - i - 1):
                if A[j] > A[j + 1]:
                    '''
                    tag = A[j]
                    A[j] = A[j + 1]
                    A[j + 1] = tag
                    '''
                    A[j], A[j+1] = A[j + 1], A[j]
        return A
                    
sort = Solution()

print(sort.sortIntegers([2,1,2,3,4,6,7]))