# -*- coding: utf-8 -*-
class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        # write your code here
        if source == target and source != None:
            return 0
        if source == None or target == None:
            return -1
        lens = len(source)
        lent = len(target)
        i = 0
        while i < lens:
            j = 0
            k = i
            flag = True
            while j < lent:
                #防止出现source = 'abcdef' target = 'defg'
                if lens - i < lent:
                    return -1
                if(source[k] != target[j]):
                    flag = False
                    break
                k = k + 1
                j = j + 1
            if flag == True:
                return i
            i = i + 1
        return -1


strs = "abcdabcdefg"
strt = "bcd"
s1 = Solution()
print(s1.strStr(strs,strt))
                    
