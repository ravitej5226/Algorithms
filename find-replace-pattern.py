# You have a list of words and a pattern, and you want to know which words in words matches the pattern.

# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

# (Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

# Return a list of the words in words that match the given pattern. 

# You may return the answer in any order.

# Example 1:

# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
# since a and b map to the same letter.

# Note:

# 1 <= words.length <= 50
# 1 <= pattern.length = words[i].length <= 20

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result=[]
        for word in words:
            if(self.checkAndReplacePattern(word,pattern)):
                result.append(word)
        return result

    def checkAndReplacePattern(self,word,pattern):
        """
        """
        pattern_dict={}
        word_dict={}
        for index in range(len(word)):
            char=pattern[index]
            char_in_word=word[index]
            if char not in pattern_dict and char_in_word not in word_dict:                
                pattern_dict[char]=word[index]
                word_dict[char_in_word]=pattern[index]

            #print(pattern_dict) 
            #print(word_dict) 
            if char_in_word not in word_dict or char not in pattern_dict or pattern_dict[char]!=char_in_word:
                #print(word)
                return False
        
        return True
        

s=Solution()
print(s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","aaa"],'abb'))