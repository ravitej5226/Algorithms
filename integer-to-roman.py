# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
class Solution(object):
    roman_integer=[1,5,10,50,100,1000]
    result=''
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        return self.computeRomanLiteral(num,5)
    
    def computeRomanLiteral(self,num,index):
        #print(num)
        if(num==0):
            return self.result
        
        current_roman_integer=self.roman_integer[index]
        

        if(num//current_roman_integer==0):
            return self.computeRomanLiteral(num,index-1)
        else:
            quotient=(int)(num/current_roman_integer)

            if(index<5):
                next_roman_integer=self.roman_integer[index+1]
            # check if substraction is possible
            
            if(index<5 and self.getSubstractedRomanLiterals(index,quotient)):
                self.result=self.result+self.getRomanLiteral(current_roman_integer)+self.getRomanLiteral(next_roman_integer)
            else:
                self.result=self.result+quotient*self.getRomanLiteral(current_roman_integer)
            
            #print(self.result)
            return self.computeRomanLiteral(num%current_roman_integer,index-1)
    
    def getSubstractedRomanLiterals(self,index,quotient):
        if(self.roman_integer[index] in [5,50,500]):
            return False;
        elif(self.roman_integer[index+1]-self.roman_integer[index]==quotient*self.roman_integer[index]):
            return True;
        return False;


    def getRomanLiteral(self,num):
        roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for literal, number in roman_dict.items():
            if(num==number):
                return literal

test=Solution()
print(test.intToRoman(94))
