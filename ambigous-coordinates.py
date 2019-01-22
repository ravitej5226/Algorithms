# We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string S.  Return a list of strings representing all possibilities for what our original coordinates could have been.

# Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

# The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

# Example 1:
# Input: "(123)"
# Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
# Example 2:
# Input: "(00011)"
# Output:  ["(0.001, 1)", "(0, 0.011)"]
# Explanation: 
# 0.0, 00, 0001 or 00.01 are not allowed.
# Example 3:
# Input: "(0123)"
# Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
# Example 4:
# Input: "(100)"
# Output: [(10, 0)]
# Explanation: 
# 1.0 is not allowed.
 

# Note:

# 4 <= S.length <= 12.
# S[0] = "(", S[S.length - 1] = ")", and the other elements in S are digits.
import decimal
class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # Get the coordinates
        c=S[1:-1]
        result=[]
        # Loop the permutations
        for i in range(1,len(c)):
            perm0=self.getPerms(c[0:i])
            perm1=self.getPerms(c[i:])
            #print(perm0)
            #print(perm1)
            result=result+['('+str(p1)+','+str(p2)+')' for p1 in perm0 for p2 in perm1]

        return result
    
    def getPerms(self,c):
       
        
        # Enforce rule for trailing 0
        if(c[0]=='0'):
            #print(c)
            perms=[] if len(c)>1 else [int(c)]
            max_iter=2 if len(c)>1 else 0
        else:
            perms=[int(c)]
            max_iter=len(c)
        
        for i in range(1,max_iter):
            if(c[-1]!='0'):
                perms.append(c[0:i]+'.'+c[i:])
        return perms

s=Solution()
print(s.ambiguousCoordinates("(0000001)"))    


    