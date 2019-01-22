# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:

# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        clean_S=[]
        clean_T=[]

        for i in range(len(S)):
            if(S[i]=='#'):
                clean_S.pop() if len(clean_S)>0 else ''
            else:
                clean_S.append(S[i])
        
        for i in range(len(T)):
            if(T[i]=='#'):
                clean_T.pop() if len(clean_T)>0 else ''          
            else:
                clean_T.append(T[i])


        return "".join(clean_S)=="".join(clean_T)

s=Solution()
print(s.backspaceCompare("ab##","c#d#"))