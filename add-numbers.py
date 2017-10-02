# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        l3 = ListNode(-1)
        while l1 != None or l2 != None:
            a = l1
            b = l2

            if a is None:
                a = ListNode(0)

            if b is None:
                b = ListNode(0)

            if head is None:
                head = ListNode(0)
            else:
                head = head.next

            if head.val==-1:
                head.val=0

            temp = head.val + a.val + b.val
            head.val = temp % 10

            if temp >= 10:
                head.next = ListNode(temp / 10)
            else:
                head.next = ListNode(-1)

            if l3.val == -1:
                l3 = head

         
            l1 = a.next
            l2 = b.next
        
        head.next=None
        while l3 != None:            
            print l3.val
            l3 = l3.next


l1 = ListNode(5)
#l1.next = ListNode(2)
#l1.next.next = ListNode(3)

l2 = ListNode(5)
#l2.next = ListNode(9)
#l2.next.next = ListNode(6)

s = Solution()
s.addTwoNumbers(l1, l2)
