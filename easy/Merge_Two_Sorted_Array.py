# -*- coding: utf-8 -*-
#两个有序数组合并
class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        lenA = len(A)
        lenB = len(B)
        C = []
        i = 0
        j = 0
        k = 0
        while i < lenA and j < lenB:
            if A[i] < B[j]:
                C.append(A[i])
                k = k + 1
                i = i + 1
            else:
                C.append(B[j])
                k = k + 1
                j = j + 1
        while i < lenA:
            C.append(A[i])
            i = i + 1
        while j < lenB:
            C.append(B[j])
            j = j + 1
        return C
    
a = [1,2,3,4,5,6,10,18]
b = [2,3,6,54,68]
s1 = Solution()
c = s1.mergeSortedArray(a,b)
print(c)