# -*- coding: utf-8 -*-
'''
写出一个高效的算法来搜索 m × n矩阵中的值。

这个矩阵具有以下特性：

每行中的整数从左到右是排序的。
每行的第一个数大于上一行的最后一个整数。

O(log(n) + log(m)) 时间复杂度
'''
class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if matrix == None:
            return False
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
            
        # write your code here
        lown = 0
        hein = len(matrix) - 1
        halfn = int((lown + hein)/2)
        n = 0
        
        lowm = 0
        heim = len(matrix[0]) - 1
        lenm = len(matrix[0]) - 1
        halfm = int((lowm + heim)/2)
        while lown <= hein:
            if matrix[halfn][lenm] < target :
                lown = halfn + 1
            elif  matrix[halfn][0] > target:
                hein = halfn - 1
            elif matrix[halfn][0] < target and matrix[halfn][lenm] > target:
                n = halfn
                break
            else:
                return True
            halfn = int((lown + hein)/2)
            print(halfn)
        while lowm <= heim :
            if matrix[n][halfm] < target:
                lowm = halfm + 1
            elif  matrix[n][halfm] > target :
                heim = halfm - 1
            else:
                return True
            halfm = int((lowm + heim)/2)
        return False

li = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
s1 = Solution()
print(s1.searchMatrix(li,1))
          