# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:

# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:

# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i=-1
        result=[]
        if(len(nums)==0):
            return result
        elif(len(nums)==1):
            result.append(str(nums[0]))
            return result

        for j in range(len(nums)-1):
            if(nums[j]+1!=nums[j+1]):
                if(j-i==1):
                    result.append(str(nums[i+1]))
                else:
                    result.append(str(nums[i+1]) + '->' + str(nums[j]))                
                i=j
        
        if(i==j):
            result.append(str(nums[i+1]))
        else:
            result.append(str(nums[i+1]) + '->' + str(nums[j+1]))                
            
        return result

                
        
        

s=Solution()
print(s.summaryRanges([0,1,4,6,7,8]))