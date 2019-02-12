# Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

# If there is no non-empty subarray with sum at least K, return -1.

 

# Example 1:

# Input: A = [1], K = 1
# Output: 1
# Example 2:

# Input: A = [1,2], K = 4
# Output: -1
# Example 3:

# Input: A = [2,-1,2], K = 3
# Output: 3
import collections;

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        result=len(A)+1
        p=[0]
        for x in A:
            p.append(p[-1]+x)
        
        queue=collections.deque()        
        
        for idx,py in enumerate(p):
            while queue and py<=p[queue[-1]]:
                queue.pop()
            
            while queue and py-p[queue[0]]>=K:
                result=min(result,idx-queue.popleft())
            
            queue.append(idx)
            
               
        return result if result<len(A)+1 else -1

s=Solution()
print(s.shortestSubarray([84,-37,32,40,95],167))