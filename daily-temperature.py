# Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

# For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

class Solution(object):
    temperature_stack=[]
    temperature_dict={}
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result=[0]*len(temperatures)        
        for index,current_temp in enumerate(temperatures):            
            if(len(self.temperature_stack)==0):
                self.push(index)
                self.temperature_dict[index]=current_temp
            else:
                while(len(self.temperature_stack)>0):
                    popped_element=self.pop()
                    if(current_temp>self.temperature_dict[popped_element]):
                        result[popped_element]=index-popped_element
                    else:
                        self.push(popped_element)                                                
                        break;
                self.push(index)
                self.temperature_dict[index]=current_temp
         
        return result                   

    
    def push(self,temperature):
        self.temperature_stack.append(temperature)
    
    def pop(self):                
        pop_element=self.temperature_stack[-1]
        self.temperature_stack=self.temperature_stack[0:-1]
        return pop_element
        
    

s=Solution();
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
#print(s.dailyTemperatures([76]*30000))