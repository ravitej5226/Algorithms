# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def computeRomanToInt(self,romanLiteral,previousValue,value):
        roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        if(romanLiteral==''):
            #print(value)
            return value;
        
        literal=romanLiteral[-1];
        currentValue=roman_dict[literal]
        if(previousValue==0):
            value=value+currentValue
        elif(previousValue>currentValue):
            value=value-currentValue
        elif(previousValue<=currentValue):
            value=value+currentValue
        romanLiteral=romanLiteral[:-1]
        #print(value)
        return self.computeRomanToInt(romanLiteral,currentValue,value)

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.computeRomanToInt(s.upper(),0,0)
       
    
    

test=Solution()
print(test.romanToInt('XIV'))