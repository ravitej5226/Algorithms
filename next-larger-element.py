# Given an array A [ ] having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array. If no such element exists, output -1 

# Input:
# The first line of input contains a single integer T denoting the number of test cases.Then T test cases follow. Each test case consists of two lines. The first line contains an integer N denoting the size of the array. The Second line of each test case contains N space separated positive integers denoting the values/elements in the array A[ ].
 
# Output:
# For each test case, print in a new line, the next greater element for each array element separated by space in order.

# Constraints:
# 1<=T<=200
# 1<=N<=1000
# 1<=A[i]<=1000

# Example:
# Input
# 1
# 4
# 1 3 2 4 

# Output
# 3 4 4 -1
def next_larger_element(arr,n):
    i=0
    j=0

    result=arr

    while(j<n or i<n):
        if(i<j):
            if(arr[i]<arr[j]):
                result[i]=str(arr[j])
                i=i+1
                j=i+1
            else:
                j=j+1
        
        if(i==j):
            j=j+1
        
        if (j>=n):
            result[i]='-1'
            i=i+1
            j=i+1
        #print('i= {0}, j={1}'.format(i,j))
    
    while(i<n):
        result[i]='-1'
        i=i+1
    
    print(' '.join(result))

# if __name__=='__main__':
#     #print(t)
#     t = input()
#     for i in range(int(t)):
#         n = int(input())
#         arr = list(map(int, input().strip().split()))
#         next_larger_element(arr,n)
#         print()
next_larger_element([10,3,12,4,2,9,13,0,8,11,1,7,5,6],14)