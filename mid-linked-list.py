# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The jud
# ge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Note:

# The number of nodes in the given list will be between 1 and 100.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution(object):
    def getMidNode(self, grid):
        # Compute length of the node
        length=0
        node=grid
        while(node!=None):
            length=length+1
            node=node.next
        
        #print(length)
        
        # Get mid index
        mid=length/2
        if(length%2!=0):
            mid=(length-1)/2
        
        #print(mid)
        mid_node=grid
        while(mid>0):
            mid_node=mid_node.next
            mid=mid-1

        # Traverse to mid node and return
        return mid_node


def createLinkedList(arr):
    head=ListNode(arr[0])
    curr=head
    for i in range(1,len(arr)):
        node=ListNode(arr[i])
        curr.next=node
        curr=curr.next
    
    return head

    
s=Solution()
head=createLinkedList([1,2,3,4,5])

print(s.getMidNode(head))

