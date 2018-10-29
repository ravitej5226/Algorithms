# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] != nums[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that nums[-1] = nums[n] = -infinity.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5 
# Explanation: Your function can return either index number 1 where the peak element is 2, 
#              or index number 5 where the peak element is 6.
# Note:

# Your solution should be in logarithmic complexity.

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=None
     
        index=0
        while index<len(nums):
            center=nums[index]

            if(index+1==len(nums)):
                right=None
            else:
                right=nums[index+1]
            # If right is greater than center
            if(right>center):                
                # Advance loop by 1
                # continue
                left=center                
                index=index+1
                
            else:
                # If right is less than center
                if(left<center):                    
                    # If left is less than center
                    # Return index
                    return index
                else:
                    # If left is greater than center
                    # Advance loop by 2
                    left=right
                    index=index+2
        
        return 0
                   
            

s=Solution()
print(s.findPeakElement([1,2,3,1]))
        