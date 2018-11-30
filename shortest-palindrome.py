# Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

# Example 1:

# Input: "aacecaaa"
# Output: "aaacecaaa"
# Example 2:

# Input: "abcd"
# Output: "dcbabcd"
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t=s+'#'+s[::-1]
        print(s)
        pi=self.getPiTable(t)
        return s[:pi[-1]-1:-1] +s

    def getPiTable(self,s):
        # Initialize pi table
        pi=[0]*(len(s)+1)
        pi[0]=-1
        
        # Initialize K
        k=-1
        s=list(s)
        s.insert(0,'-1')
        
        for i in range(1,len(s)):
            while(k>=0 and s[k+1]!=s[i]):
                k=pi[k]                                
            k=k+1
            pi[i]=k
        
        return pi
    

s=Solution();
print(s.shortestPalindrome("abcd"))