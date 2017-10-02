import math
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        hash_str='$'
        print s
        for i in range(len(s)):
            hash_str=hash_str+'#'+s[i]            
        
        hash_str=hash_str+'#'+'@'
        
        # initialize p array
        p=[0]*len(hash_str)
        c=1
        m=0
        r=1
        max_length=0
        max_length_palindrome=''
        for i in range(1,len(hash_str)-1):
            m=2*c-i

            # if current index is within boundaries of the current palindrome being considered
            # initialize the p[i] based on the mirror count or right boundary index
            if i<r:
                p[i]=min(r-i,p[m])
            
            temp_str=''

            if(hash_str[i]!='#'):
                temp_str=hash_str[i]
          #  print temp_str
            # Compare the mirrors and update palindrome length if same
            while hash_str[i+1+p[i]]==hash_str[i-1-p[i]]:
                
                if hash_str[i+1+p[i]] != '#':
                    temp_str=hash_str[i+1+p[i]]+temp_str+hash_str[i+1+p[i]]
                p[i]=p[i]+1
            
            #print temp_str
            # If right boundary of the palindrome at current index exceeded the 
            # right boundary of current palindrome, update the center and right boundary
            # and consider newly found palindrome as current palindrome
            if i+p[i]>r:
                c=i
                r=c+p[i]
            print p
            if max_length<p[i]:
                max_length=p[i]
                max_length_palindrome=''
                t1=i
                r1=r

               # print i
                #print r                

                if hash_str[t1] !='#':
                    max_length_palindrome=hash_str[t1]
                
                print max_length_palindrome
                t1=t1+1
                while t1<r1:
                    if hash_str[t1] != '#':
                        max_length_palindrome=hash_str[t1]+max_length_palindrome+hash_str[t1]
                    t1=t1+1

            
        print max_length_palindrome
        

s=Solution()
s.longestPalindrome('ababaca')