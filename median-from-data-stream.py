# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

# For example,
# [2,3,4], the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:

# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
 

# Example:

# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
 

# Follow up:

# If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
import math
class MedianFinder(object):

    num_list=[]
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.num_list=[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        index=0

        if(len(self.num_list)>0):
            index=self.getIndex(0,len(self.num_list),num)
        
        self.num_list.insert(index,num)
        
    
    def getIndex(self,min,max,num):
        if(min==max-1):
            return min if self.num_list[min]>num else max
        print('min '+str(min))
        print('max '+str(max))
        print('num '+str(num))
        index=math.ceil((float)(min+max)/2)
        index=(int)(index)
        if(self.num_list[index]>num):
            return self.getIndex(min,index,num)
        else:
            return self.getIndex(index,max,num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        count=len(self.num_list)

        if(count%2!=0):
            return self.num_list[count/2]
        else:
            floor=(int)(math.floor(count/2.0))
            ceil=(int)(math.ceil(count/2.0))-1
            print(floor)
            print(ceil)
            return (float)((self.num_list[floor]+self.num_list[ceil])/2.0)

        return self.num_list[0]
        


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()

obj.addNum(5)
obj.addNum(2)
obj.addNum(1)
obj.addNum(52)

obj.addNum(5)
obj.addNum(45)

obj.addNum(544)
obj.addNum(6)
param_2 = obj.findMedian()
print(param_2)
print(obj.num_list)