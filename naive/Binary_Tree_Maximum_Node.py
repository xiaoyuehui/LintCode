# -*- coding: utf-8 -*-
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
    def insertLeftNode(self,tree):
        if self.left == None:
            self.left = tree
        else:
            tf = tree
            tf.left = self.left
            self.left = tf
        
    def insertrightNode(self,tree):
        if self.right == None:
            self.right = tree
        else:
            tr = tree
            tr.right = self.right
            self.right = tr
            
    def getLeftTree(self,tree):
        return tree.left
    
    def getRightTree(self,tree):
        return tree.right

class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """
    #返回值最大的节点....这是入门题？？？？？
    numlist = []
    def maxNode(self, root):
        if root:
            lefttree = self.maxNode(root.left)
            righttree = self.maxNode(root.right)
            return self.treemax(root,self.treemax(lefttree,righttree))
        
    def treemax(self,left,right):
        if left == None:
            return right
        if right == None:
            return left
        if left.val > right.val:
            return left
        if left.val <= right.val:
            return right


tree=TreeNode(1)
tree.insertLeftNode(TreeNode(2))
tree.insertrightNode(TreeNode(3))

leftchild = tree.getLeftTree(tree)
rightchild = tree.getRightTree(tree)

leftchild.insertrightNode(TreeNode(4))
rightchild.insertLeftNode(TreeNode(5))
rightchild.insertrightNode(TreeNode(6))


s1 = Solution()
s1.maxNode(tree)
print(s1.maxNode(tree).val)