# Given an integer matrix, find the length of the longest increasing path.

# From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

# Example 1:

# Input: nums = 
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:

# Input: nums = 
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if(len(matrix)==0):
            return 0
        result=1
        self.rows=len(matrix)
        self.columns=len(matrix[0])
        self.matrix=matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                #print('--------------------')                
                visited=[(i,j)]                
                result=max(result,self.getMaxPath((i,j),visited,1))
                
            
        return result
    
    def getMaxPath(self,current,visited,pathCount):
        # Get the max left, right, top, bottom and 
        # Return pathCount+max
        
        left_count=right_count=top_count=bottom_count=pathCount
        #print(current,pathCount,self.matrix[current[0]][current[1]])
        #print(visited)
        # Check top
        if(current[0]-1>=0 and (current[0]-1,current[1]) not in visited and self.matrix[current[0]-1][current[1]]>self.matrix[current[0]][current[1]]):
            #print(self.matrix[current[0]-1][current[1]],self.matrix[current[0]][current[1]])
            a=visited[:]
            a.append((current[0]-1,current[1]))
            top_count=self.getMaxPath((current[0]-1,current[1]),a,pathCount+1)
        
        # Check bottom
        if(current[0]+1<self.rows and (current[0]+1,current[1]) not in visited and self.matrix[current[0]+1][current[1]]>self.matrix[current[0]][current[1]]):
            #print(self.matrix[current[0]+1][current[1]],self.matrix[current[0]][current[1]])
            a=visited[:]
            a.append((current[0]+1,current[1]))
            bottom_count=self.getMaxPath((current[0]+1,current[1]),a,pathCount+1)

        # Check left
        if(current[1]-1>=0 and (current[0],current[1]-1) not in visited and self.matrix[current[0]][current[1]-1]>self.matrix[current[0]][current[1]]):
            #print(self.matrix[current[0]][current[1]-1],self.matrix[current[0]][current[1]])
            a=visited[:]
            a.append((current[0],current[1]-1))
            left_count=self.getMaxPath((current[0],current[1]-1),a,pathCount+1)

        # Check right
        if(current[1]+1<self.columns and (current[0],current[1]+1) not in visited and self.matrix[current[0]][current[1]+1]>self.matrix[current[0]][current[1]]):
            #print(self.matrix[current[0]][current[1]+1]>self.matrix[current[0]][current[1]])
            a=visited[:]
            a.append((current[0],current[1]+1))
            right_count=self.getMaxPath((current[0],current[1]+1),a,pathCount+1)

        return max(left_count,right_count,top_count,bottom_count)
                
        
    

s=Solution()
print(s.longestIncreasingPath([
    [7,8,9],
    [9,7,6],
    [7,2,3]]  ))