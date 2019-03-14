# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

# Example 1:

# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        result=[-1]*len(S)
        anchor=-1
        for idx,i in enumerate(S):
            if(i==C):
                result[idx]=0
                r=anchor+1 if anchor==-1 else anchor
                for x in range(r,idx):
                    print(result)
                    result[x]=min(x-anchor,idx-x) if anchor!=-1 else idx-x
                anchor=idx
        for x in range(anchor,len(S)):
                    print(result)
                    result[x]=x-anchor
        return result

s=Solution()
print(s.shortestToChar("aaba","b"))