# Given a binary tree, find the leftmost value in the last row of the tree.

# Example 1:
# Input:

#     2
#    / \
#   1   3

# Output:
# 1
# Example 2: 
# Input:

#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7

# Output:
# 7
# Note: You may assume the tree (i.e., the given root node) is not NULL.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findLeaf(root,0)[0]        
    
    def findLeaf(self,root,index):
        if(root.left is None and root.right is None):
            return (root.val,index)
        else:
            rightBottom=None
            leftBottom=None
            if(root.left is not None):
                leftBottom=self.findLeaf(root.left,index+1)
            
            if(root.right is not None):
                rightBottom=self.findLeaf(root.right,index+1)
            
            if(leftBottom is None):
                print(leftBottom)
                return rightBottom
            else:
                print(rightBottom)
                return leftBottom
            if(leftBottom[1]>=rightBottom[1]):
                return leftBottom
            else:
                return rightBottom


    def createBinaryTree(self,arr):
        tree=None
        for index in range(len(arr)):
            node=TreeNode(arr[index])
            print(node)
            tree=self.addNode(node,tree)
        return tree

    def addNode(self,node,btree):
        if(btree is None):
            btree=node
            return btree
        else:
            if(btree.val>node.val):
                btree.left=self.addNode(node,btree.left)
                return btree
            else:                
                btree.right= self.addNode(node,btree.right)
                return btree

s=Solution()
tree=s.createBinaryTree([2,1,3])
print(s.findBottomLeftValue(tree))
        