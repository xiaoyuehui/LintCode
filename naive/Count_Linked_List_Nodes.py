# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.lastNode = self
        
    def addNode(self , listnode):
        self.lastNode.next = listnode 
        self.lastNode = listnode
    
    def PirntNodeValue(self):
        nextnode = self
        while nextnode!=None:
            print('->' + str(nextnode.val))
            nextnode = nextnode.next
            
class Solution:
    """
    @param: head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        # write your code here
        if head == None:
            return 0
        tem = head
        node_count = 1
        while tem.next != None:
            node_count = node_count + 1
            tem = tem.next
        return node_count
    
    
l1 = ListNode(5)
l1.addNode(ListNode(6))
l1.addNode(ListNode(6))

s1 = Solution()
print(s1.countNodes(l1))
            
