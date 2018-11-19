# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
# Note:

# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return 0
        results=[0]*len(nums)
        results[0]=1
        maxLength=1
        for index in range(1,len(nums)):            
            maxval=0
            for j in range(index):
                if(nums[index]>nums[j]):
                    maxval=max(maxval,results[j])
            
            results[index]=maxval+1                
            maxLength=max(maxLength,results[index])
            
                
        return maxLength

s=Solution()
print(s.lengthOfLIS([10,9,2,5,3,4]))
