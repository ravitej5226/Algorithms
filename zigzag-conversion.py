# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        output=[];
        if s=='':
            output=''  
            return output     
        if numRows==1:
            return s 
        for i in range(0,numRows):
            start_index=i;     
            alt=True;
            temp=0
            if start_index<len(s):
                output.append(s[start_index]);
            else:
                break; 
            while start_index<len(s):                
                if temp>0:
                    output.append(s[start_index]);

                if(alt):
                    temp=2*(numRows-1-i);
                else:
                    temp=2*(i);
                start_index=start_index+temp;                
                alt=not alt;
                
            
                
        return ''.join(output)
s=Solution();
print s.convert('pa',2);
