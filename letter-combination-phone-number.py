# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """        
        # Create dictionary
        letter_dict = {2: "abc", 3: "def", 4: "ghi", 5: "jkl",
                       6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        
        if(len(digits)==0):
            return []       

        result=list(letter_dict[int(digits[0])])

        for idx,x in list(enumerate(digits))[1:]:            
            result=[a+b for a in result for b in list(letter_dict[int(x)])]
            

        # Read the digits in a list
        return result


s = Solution()
print(s.letterCombinations("29"))
