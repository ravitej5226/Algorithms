# Given an n-ary tree, return the postorder traversal of its nodes' values.

# For example, given a 3-ary tree:

 
#             1
#     3       2       4

# 5       6
 

# Return its postorder traversal as: [5,6,3,2,4,1].

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        #if(root is None):
         #   return
        if(len(root.children)==0):
            return [root.val]
        else:
            result=[]
            
            for i in root.children:
                #print(root.val)
                result =result+ (self.postorder(i))
            result.append(root.val)
            return result

def createRoot(data):
    # Read data of children and val
    # Call Create root for each children
    
    val=data["val"]
    children=[]
    for item in data["children"]:
        children.append(createRoot(item))
    return Node(val,children)
    


s=Solution()
#print(s.postorder(None))
a=createRoot({"$id":"1",
"children":[
    {"$id":"2","children":[
        {"$id":"5","children":[],"val":5},
        {"$id":"6","children":[],"val":6}],
        "val":3},
    {"$id":"3","children":[],"val":2},
    {"$id":"4","children":[],"val":4}
    ],
"val":1})
print(s.postorder(a))