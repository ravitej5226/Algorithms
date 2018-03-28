# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    def computeRomanToInt(self,romanLiteral,previousValue,value):        
        if(romanLiteral==''):
            #print(value)
            return value;
                
        literal=romanLiteral[-1];
        currentValue=self.roman_dict[literal]
        if(previousValue>currentValue):
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
        return self.computeRomanToInt(s[:-1].upper(),self.roman_dict[s[-1]],self.roman_dict[s[-1]])
       
    
    

test=Solution()
print(test.romanToInt('XIV'))