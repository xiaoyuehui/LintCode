class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of intege
    returnlist = []
    
    def flatten(self, nestedList):
        # Write your code here
        if type(nestedList) == type(1):
            return [nestedList]
        for i in range(len(nestedList)):
            if type(nestedList[i]) != type(list()):
                self.returnlist.append(nestedList[i])
            else:
                self.flatten(nestedList[i])
        return self.returnlist
                
nestedList = [[1,1],2,[1,1]]           
s1 = Solution()
newlist = s1.flatten(nestedList)
print(newlist)