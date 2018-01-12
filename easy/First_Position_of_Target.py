# -*- coding: utf-8 -*-
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        if nums == None or len(nums) == 0:
            return -1
        low = 0
        height = len(nums) - 1
        while low <= height:
            half = int((low + height)/2)
            if nums[half] < target:
                low = half + 1
            if nums[half] > target:
                height = half - 1
            if nums[half] == target:
                #如果存在重复数字则可能报错
                index = half - 1
                while nums[index] == target:
                    index = index - 1
                    half = half - 1
                return half;
        return -1


nums = [1,2,2,2,3,4,5,6,7]
s1 = Solution()
print(s1.binarySearch(nums,1))