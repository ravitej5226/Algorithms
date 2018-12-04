import math
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Preprocess the string to include delimiters
        hash_string=self.preprocess(s)
        
        # Initialize the P array
        # Initialize C, R
        palindrome_lengths=[]
        center_index=0
        right_index=0        

        # Loop each index
        for current_index in range(len(hash_string)):
            if(current_index==0 or current_index==len(hash_string)-1):
                palindrome_lengths.append(0)
                continue

            # Get the mirror index
            current_index_mirror=center_index-(current_index-center_index)

            if(current_index>right_index):
                center_index=current_index

            # Set initial value for palindrome length
            
            palindrome_lengths.append(0)

            while(palindrome_lengths[current_index]+1+center_index<len(hash_string) and hash_string[palindrome_lengths[current_index]+1+center_index]==hash_string[center_index-1-palindrome_lengths[current_index]]):
                palindrome_lengths[current_index]=palindrome_lengths[current_index]+1            
        
        return palindrome_lengths
    
    def preprocess(self,s):
        hash_string='#'
        for index in range(len(s)):
            hash_string=hash_string+s[index]+'#'
        return hash_string

s=Solution()
print(s.longestPalindrome('ababaca'))