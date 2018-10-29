# Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

# For example, 

# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
# And the value to insert: 5
# You can return this binary search tree:

#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5
# This tree is also valid:

#          5
#        /   \
#       2     7
#      / \   
#     1   3
#          \
#           4

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node=TreeNode(val)
        root=self.insert(root,node)
        return root

    def insert(self,root,node):
        if(root.val>node.val):
            if(root.left is None):
                root.left=node
                return root
            else:
               return self.insert(root.left,node)
        else:
            if(root.right is None):
                root.right=node
                return root
            else:
               return self.insert(root.right,node)

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


s=Solution();
root=stringToTreeNode("[4,2,7,1,3]")
print(s.insertIntoBST(root,5))