# Algorithm to illustrate KMP algorithm

class Solution:
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
        print(pi)
        return pi
    
    def doesPatternExist(self,s,p):
        pi=self.getPiTable(p)
        p='1'+p
                
        k=0
        for i in range(len(s)):
            c=s[i]
            
            while(k>=0 and p[k+1]!=c):
                k=pi[k]
            k=k+1
            if(k==len(p)-1):
                return i-len(p)-1
        return -1



s=Solution()
print(s.doesPatternExist('abc abcdab abcdabcdabde','abcdabd'))