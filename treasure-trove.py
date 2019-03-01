# There is a maze of m X m size, each will have an alphabet from ‘A’ to ‘Z’ (for ease of calculation m is
# odd). ‘T’ represents Treasure, X represents the passage. The treasure is placed in the centre of the
# maze (e.g. for a 5 X 5 maze, treasure is at 3rd row & 3rd Column). Only way to reach the treasure is from
# the top left corner of the maze & the entry is allowed to next layer only if top left corner has passage
# (‘X’). Your aim is to find the minimum number of steps each layer of the maze to be rotated counter
# clockwise (+ve) /clockwise (-ve) so that all ‘X’ come to the left corner & treasure can be reached.
# E.g.
# The input Maze
#  0 1 2 3 4 5 6
# 0 L E A R K X G
# 1 N Z N Z Q B S
# 2 O P E B M S I
# 3 A Z R T X M U
# 4 A W S S O K U
# 5 A X B A G M O
# 6 D F Q A C U U
# First layer is the text mentioned in Blue colour, Second layer is the text mentioned in Red colour , Third
# in Green, ’T’ is the treasure. To reach the Treasure from top left, you need to rotate first layer counter
# clockwise 5 times, Red layer Clock wise 4 times (-4), and Green one by ‘3’ counter clockwise. This
# makes ‘X’ in first layer to reach [0][0] position, [1][1] position & [2][2] position.
# It is guaranteed that ‘T’ is only in the center of the maze
# It is guaranteed that only one ‘X’ is present in each of the layer
# 1 <= Size of maze(m) <= 99, maze is always m X m and m is odd
# Memory consumption can be liberal, but O(N) is the tie breaker

# You need to output
# 1. No of rotations of each layer, +ve represents counter clockwise & -ve represents clockwise.
# 2. Output of the resultant maze after transformations(below is the example of given input maze)
# 5 -4 3
#  0 1 2 3 4 5 6
# 0 X G S I U U O
# 1 K X W Z P Z U
# 2 R B X O S N U
# 3 A A M T S Z C
# 4 E G B E R Q A
# 5 L M K M S B Q
# 6 N O A A A D F

class Solution(object):
    def treasureTrove(self,matrix):        
        # Find number of layers
        layer_count=int(len(matrix)/2)+1
        matrix_order=len(matrix[0])
        layer_coordinates=[(x,x,(matrix_order-x*2)*4-4) for x in range(layer_count)]
        layer_coordinates.pop()
        layer_data=[]
        layer_arrangement=[]
        layer_steps=[]
        for layer in layer_coordinates:            
            row=layer[0]
            column=layer[1]
            count=layer[2]
            data=[matrix[row][column]]                        
            boundary=matrix_order-1-layer[0]
            path_index=0
            steps=[(row,column)]

            # We go clockwise all the time to find 'X'
            column=column+1
            for i in range(count-1):                
                data.append(matrix[row][column])
                steps.append((row,column))
                if(matrix[row][column]=='X'):
                    path_index=i+1

                if(column==boundary and row!=boundary):
                    row=row+1
                elif(row==boundary and column>layer[1]):
                    column=column-1
                elif(column==layer[1]):
                    row=row-1
                else:
                    column=column+1
            layer_steps.append(steps)

            # Compute the shortest arrangement
            if(path_index>len(data)/2):
                # clockwise
                layer_arrangement.append((len(data)-path_index)*-1)
            else:
                layer_arrangement.append(path_index)

            layer_data.append(data)
        
        for idx,i in enumerate(layer_arrangement):
            temp=layer_data[idx]
            if(i<0):
                i=i+len(temp)
            data=temp[i:]+temp[:i]
            step=layer_steps[idx]
            for index,val in enumerate(data):
                current_step=step[index]
                matrix[current_step[0]][current_step[1]]=val

        return layer_arrangement,matrix

    def printMatrix(self,matrix):
        for row in range(len(matrix)):
            print (' '.join(matrix[row]))

        

s=Solution()
matrix=[['L','E','A','R','K','X','G'],['N','Z','N','Z','Q','B','S'],['O','P','E','B','M','S','I'],['A','Z','R','T','X','M','U'],
['A','W','S','S','O','K','U'],['A','X','B','A','G','M','O'],['D','F','Q','A','C','U','U']];

print("\n")
s.printMatrix(matrix)
result=s.treasureTrove(matrix)
print("\nResult:")
print(result[0])
s.printMatrix(result[1])