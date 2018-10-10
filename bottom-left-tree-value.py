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
                return rightBottom
            elif(rightBottom is None):                
                return leftBottom
                
            if(leftBottom[1]>=rightBottom[1]):
                return leftBottom
            else:
                return rightBottom


# Sample code that creates a binary tree
def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

s=Solution()
tree=stringToTreeNode("[1,2,3,4,null,5,6,null,null,7]")
print(s.findBottomLeftValue(tree))
        