# It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by  from  at the front of the line to  at the back.

# Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if and  bribes , the queue will look like this: .

# Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!

# Function Description

# Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.

# minimumBribes has the following parameter(s):

# q: an array of integers
# Input Format

# The first line contains an integer , the number of test cases.

# Each of the next  pairs of lines are as follows: 
# - The first line contains an integer , the number of people in the queue 
# - The second line has  space-separated integers describing the final state of the queue.

# Constraints

# Subtasks

# For  score 
# For  score 

# Output Format

# Print an integer denoting the minimum number of bribes needed to get the queue into its final state. Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than  people.

# Sample Input

# 2
# 5
# 2 1 5 3 4
# 5
# 2 5 1 3 4
# Sample Output

# 3
# Too chaotic
# Explanation

# Test Case 1

# The initial state:

# pic1(1).png

# After person  moves one position ahead by bribing person :

# pic2.png

# Now person  moves another position ahead by bribing person :

# pic3.png

# And person  moves one position ahead by bribing person :

# pic5.png

# So the final state is  after three bribing operations.

# Test Case 2

# No person can bribe more than two people, so its not possible to achieve the input state.
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    idx=0
    j=0
    count=0
    while(idx<len(q)):
        i=q[idx]
        #print('-- ',q,idx)
        # Check for error
        if(abs(i-(idx+1))>2):
            #print(i,idx)            
            print('Too Chaotic')
            return
        if(i!=idx+1):
                
            # Check if next element is smaller    
            # If no, set J and increment idx
            if(i<q[idx+1]):
                
                idx=idx+1
            else:            
                # If yes, move till element at idx reaches proper position
                q[idx]=q[idx+1]
                q[idx+1]=i
                count=count+1
                # temp=q[idx+1]
                # for x in range(i-1):
                #     if(x+idx+1<len(q)):
                #         q[x+idx]=q[x+idx+1]
                #         count=count+1
                # q[i-1]=i
                idx=j
        else:
            j=idx
            idx=idx+1
    print(count)

t=[[2,5,1,3,4],[2,1,5,3,4],[1,2, 5, 3, 7, 8, 6,4],[1, 2, 5, 3, 4, 7, 8, 6]]
for i in t:
    print(i)
    print(minimumBribes(i))

#[2,1,5,3,4]

# count=0
#     for idx,i in enumerate(q):
#         print(abs(i-(idx+1)))
#         print(q)
#         if(abs(i-(idx+1))>2):
#             #print(i,idx)            
#             print('Too Chaotic')
#             return
#         elif(i!=idx+1):
#             temp=idx
#             for x in range(i-1):
#                 if(x+idx+1<len(q)):
#                     q[x+idx]=q[x+idx+1]
#                     count=count+1
                
        
#             q[i-1]=i
#     print(count)        
#     return True

 #   return q
