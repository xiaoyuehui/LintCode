class Solution:
    """
    @param: n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        #时间复杂度为n*n
        '''
        if n > 2 :
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)
        if n == 2:
            return 1
        if n == 1:
            return 0
        '''
        
        #时间复杂度为n
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n > 2:
            num1 = 0
            num2 = 1
            num = 2
            while(num < n - 1):
                num2 = num1 + num2
                num1 = num2 - num1
                num = num + 1
            return num1 + num2
            
        
s1 = Solution()
    
print(s1.fibonacci(10))