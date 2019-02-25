# Given an array A, partition it into two (contiguous) subarrays left and right so that:

# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

 

# Example 1:

# Input: [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
# Example 2:

# Input: [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]
 

# Note:

# 2 <= A.length <= 30000
# 0 <= A[i] <= 10^6
# It is guaranteed there is at least one way to partition A as described.
class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if(len(A)==2):
            return 1
        i=0
        j=len(A)-1
        left_max=0
        while(j>0):
            if(A[j]>=A[0]):
                j=j-1
            else:
                break
        
        # Compute left_max
        for x in range(j):
            left_max=max(left_max,A[x])
        #print(left_max)
        #print(j)
        
        if(j==0):
            return 1

        # From j to max, include all elements which are less than left max        
        t=False        
        while(j<len(A)-1):
            if(left_max>=A[j]):
                t=True
                j=j+1
            else:
                break
        #print(left_max)
        
        return j+1 if not t else j-1 if left_max==A[j-1] else j


s=Solution()
print(s.partitionDisjoint([0,7,11,1,12,2,13,96,34,18,82,37,98,68,90,61,20,94,21,86]))
        
# [26,51,40,58,42,76,30,48,79,91]

# [63,18,8,31,0,21,40,81,100,88,72,82,68,99,73]

# [6,0,8,30,37,6,75,98,39,90,63,74,52,92,64]

# [3,1,8,4,9,7,12,0,0,12,6,12,6,19,24,90,87,54,92,60,31,59,75,90,20,38,52,51,74,70,86,20,27,91,55,47,54,86,15,16,74,32,68,27,19,54,13,22,34,74,76,50,74,97,87,42,58,95,17,93,39,33,22,87,96,90,71,22,48,46,37,18,17,65,54,82,54,29,27,68,53,89,23,12,90,98,42,87,91,23,72,35,14,58,62,79,30,67,44,48]

# [12,75,26,38,56,59,83,55,49,52,27,48,77,21,27,79,54,15,59,22,34,35,81,67,2,41,40,0,73,61,75,8,86,42,49,83,43,16,2,54,26,35,15,63,31,24,51,86,6,35,42,37,83,51,34,21,71,57,61,76,50,1,43,32,19,13,67,87,3,33,38,34,34,84,38,76,52,7,27,49,2,78,56,28,70,6,64,87,100,97,99,97,97,100,100,100,97,89,98,100]


#[0,7,11,1,12,2,13,96,34,18,82,37,98,68,90,61,20,94,21,86]