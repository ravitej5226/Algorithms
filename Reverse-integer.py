# Reverse digits of an integer. 
# Status: INCOMPLETE

# Example1: x = 123, return 321
# Example2: x = -123, return -321

# Note:
# The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result=0;
        index=0
        while x/10!=0:
            temp=x%10;
            result=result*(10^index)+temp;
            x=x/10;
            index=index+1;
        
       
        temp=x%10;
        result=result*(pow(10,index))+temp;
        x=x/10;
        
        return result
        

s=Solution();
print(s.reverse(103))