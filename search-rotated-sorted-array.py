# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Check if solution is before pivot (bp) or after pivot (ap) -1->bp, 1->ap
        target_trend=-1

        if(len(nums)==0):
            return -1
        
        

        if(nums[0]>target):
            target_trend=1
        
        index=self.get_target(nums,0,len(nums)-1,target,target_trend,nums[0])
        return index
    
    def get_target(self,nums,min,max,target,target_trend,first_element):
        if(len(nums[min:max+1])==1):
            return min if nums[min]==target else -1

        if(len(nums[min:max+1])==2):
            if(nums[min]==target):
                return min
            elif(nums[max]==target):
                return max
            else:
                return -1

        # Get mid index
        mid=(min+max)/2
        
        if(nums[mid]==target):
            return mid
        
        if(min==max):
           return -1
        
        trend=0

        if(nums[mid-1]<nums[mid] and nums[mid]<nums[mid+1]):
            if(nums[mid-1]>=first_element):
                trend=-1
            else:
                trend=1
        else:
            trend=0
        
        if(trend==-1):
            if(target_trend==1):
                #print('next half')
                return self.get_target(nums,mid+1,max,target,target_trend,first_element)
            else:
                if(nums[mid]>target):
                    #print('prev half')
                    return self.get_target(nums,min,mid-1,target,target_trend,first_element)
                else:
                    #print('next half')
                    return self.get_target(nums,mid+1,max,target,target_trend,first_element)
        elif(trend==1):
            if(target_trend==1):
                if(nums[mid]>target):
                    #print('prev half')
                    return self.get_target(nums,min,mid-1,target,target_trend,first_element)
                else:
                    #print('next half')
                    return self.get_target(nums,mid+1,max,target,target_trend,first_element)
            else:
                #print('prev half')
                return self.get_target(nums,min,mid-1,target,target_trend,first_element)
        else:
            if(target_trend==1):
                #print('next half')
                return self.get_target(nums,mid+1,max,target,target_trend,first_element)
            else:
                #print('prev half')
                return self.get_target(nums,min,mid-1,target,target_trend,first_element)





        #return trend
        

        # If there is no mid point, compare and return


s=Solution()
print(s.search([1,3,5],5))