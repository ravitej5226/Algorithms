# Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

# We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

# (Note also that a translation does not include any kind of rotation.)

# What is the largest possible overlap?

# Example 1:

# Input: A = [[1,1,0],
#             [0,1,0],
#             [0,1,0]]
#        B = [[0,0,0],
#             [0,1,1],
#             [0,0,1]]
# Output: 3
# Explanation: We slide A to right by 1 unit and down by 1 unit.
# Notes: 

# 1 <= A.length = A[0].length = B.length = B[0].length <= 30
# 0 <= A[i][j], B[i][j] <= 1

class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        rows=len(A[0])

        overlap=0

        # For each traversal to left
        for i in range(rows):
            for j in range(rows):
            # Traverse all the way to down and check overlaps
               
                forward_A=''.join([''.join("{0}".format(n) for n in x[0:rows-i]) for x in A[0:rows-j] ])
                forward_B=''.join([''.join("{0}".format(n) for n in x[i:]) for x in B[j:] ])
                #print(int(new_A,base=2))
                #print(int(new_B,base=2))
                # print('i,j = {0}, {1}'.format(i,j))
                # print(forward_A)
                # print(forward_B)
                forward_result=['1' if x==y=='1' else '0' for x,y in zip(forward_A,forward_B)]
                overlap=max(overlap,forward_result.count('1'))

                backward_A=''.join([''.join("{0}".format(n) for n in x[i:]) for x in A[j:] ])
                backward_B=''.join([''.join("{0}".format(n) for n in x[:rows-i]) for x in B[:rows-j] ])
                
                new_result=['1' if x==y=='1' else '0' for x,y in zip(backward_A,backward_B)]
              
                
                

                overlap=max(overlap,new_result.count('1'))
        return overlap

s=Solution()
print(s.largestOverlap([[0,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,1,0,0,1]],
[[1,0,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,1],[1,0,1,1,1]]))

