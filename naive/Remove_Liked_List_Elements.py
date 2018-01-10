# -*- coding: utf-8 -*-

#Definition for singly-linked list.
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
    @param: head: a ListNode
    @param: val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # write your code here
        if head == None:
            print('List is empty!')
            return
        while head != None and head.val == val:
            head = head.next
            
        pre = None
        tem = head
        if tem == None:
            return None
        
        #head.PirntNodeValue()
        #print('----')
        #tem.PirntNodeValue()

        flag = 1
        while tem.next != None:
            print(tem.val)
            if flag:
                pre = tem
                tem = tem.next
            flag = 1
            if tem.val == val:
                print('ok')
                if tem.next == None:
                    #如果最后一个元素的值与传入的值相同，则删除节点
                    if(tem.val == val):
                        pre.next = None
                    break
                else:
                    tem = tem.next
                    pre.next = tem
                    if tem.next == None:
                        if(tem.val == val):
                            pre.next = None
                        break
                    flag = 0
        return head
                


l1 = ListNode(5)
l1.addNode(ListNode(6))
l1.addNode(ListNode(6))


s1 = Solution()
l2 = s1.removeElements(l1,6)
l2.PirntNodeValue()

