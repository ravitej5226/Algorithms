# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

# For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
# OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
# That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# Return the length of a maximum size turbulent subarray of A.


# Example 1:

# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
# Example 2:

# Input: [4,8,12,16]
# Output: 2
# Example 3:

# Input: [100]
# Output: 1


# Note:

# 1 <= A.length <= 40000
# 0 <= A[i] <= 10^9

class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # If length is less than or equal to 2
        if(len(A) <= 1):
            # Return length of the array
            return len(A)
        elif (len(A) == 2):
            return 1 if A[1]==A[0] else 2

        else:
            # Else
             # Initialize index to 1
            index = 1

            # Intialize result object to 2
            result = 2 if A[index] != A[index-1] else 1

            # Initialize streak object to 2
            streak = result

            # Initialize trend
            trend = A[index] > A[index-1]
            index = index+1

            # While index is less than length of array
            while(index < len(A)):
                # Compute the current trend
                current = A[index] > A[index-1]

                # If current XOR trend is true
                if(current != trend and A[index] != A[index-1]):
                    # print(A[index])
                    # Increment streak by 1
                    streak = streak+1
                else:
                    # Else
                    # Set result to MAX(streak, result)
                    result = max(result, streak)

                    # Reset streak to 2
                    streak = 2 if A[index] != A[index-1] else 1
                trend = current
                index = index+1

            # Return result
            return max(result, streak)


s = Solution()
print(s.maxTurbulenceSize([422,204,396,362,440,114,350,283,449,72,397,380,277,334,433,93,343,24,374,255,244,158,482,28,358,467,223,403,264,291,350,256,47,117,476,230,93,122,140,169]))
