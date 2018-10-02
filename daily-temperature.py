# Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

# For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

class Solution(object):
      
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result=[0]*len(temperatures)        
        temperature_stack=[]  
        for index in xrange(len(temperatures)-1,-1,-1):            
            current_temperature=temperatures[index]
            if(len(temperature_stack)==0):
                temperature_stack.append(index)
            else:                
                popped_index=temperature_stack.pop()
                popped_temperature=temperatures[popped_index]
                while(current_temperature>=popped_temperature and len(temperature_stack)>0):
                    popped_index=temperature_stack.pop()
                    popped_temperature=temperatures[popped_index]
                
                if(popped_temperature>current_temperature):
                    result[index]=popped_index-index
                    temperature_stack.append(popped_index)                    
                else:
                    result[index]=0            
                temperature_stack.append(index)
        
        return result                   

    
s=Solution();
print(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
