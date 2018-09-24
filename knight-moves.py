# Given a square chessboard of N x N size, the position of Knight and position of a target is given. We need to find out minimum steps a Knight will take to reach the target position.

# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the square chessboard. The next line contains the X-Y coordinates of the knight. The next line contains the X-Y coordinates of the target. 

# Output:
# Print the minimum steps the Knight will take to reach the target position.

# Constraints:
# 1<=T<=100
# 1<=N<=20
# 1<=knight_pos,targer_pos<=N

# Example:
# Input:
# 2
# 6
# 4 5
# 1 1
# 20
# 5 7
# 15 20

# Output:
# 3
# 9

results=[]
moves={}
import time
start_time = time.time()
def calculateMoves(x_target,y_target,x_knight,y_knight,board_size,counter):
    if((x_knight<1 or y_knight<1) or (len(results)>0 and counter >= max(results))):
        return;
    if(x_target==x_knight and y_target==y_knight):
        print(results)
        results.append(counter);
        print(len(moves))
    else:
        # Work on top right
        # check boundaries and return accordingly
        x_temp=x_knight+1
        y_temp=y_knight+2

        if (not(x_temp>board_size or y_temp > board_size) and x_temp>0 and y_temp>0):      
            if((x_temp,y_temp) in moves):
                if(moves[(x_temp,y_temp)]>counter+1):
                    moves[(x_temp,y_temp)]=counter+1
                    calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)
            else:
                moves[(x_temp,y_temp)]=counter+1
                calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)

        # Work on top left
        x_temp=x_knight-1
        y_temp=y_knight+2

        if (not(x_temp>board_size or y_temp > board_size) and x_temp>0 and y_temp>0):           
            if((x_temp,y_temp) in moves):
                if(moves[(x_temp,y_temp)]>counter+1):
                    moves[(x_temp,y_temp)]=counter+1
                    calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)
            else:
                moves[(x_temp,y_temp)]=counter+1
                calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)

        # Work on side top right
        x_temp=x_knight+2
        y_temp=y_knight+1

        if (not(x_temp>board_size or y_temp > board_size) and x_temp>0 and y_temp>0):       
            if((x_temp,y_temp) in moves):
                if(moves[(x_temp,y_temp)]>counter+1):
                    moves[(x_temp,y_temp)]=counter+1
                    calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)
            else:
                moves[(x_temp,y_temp)]=counter+1
                calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)

        # Work on side top left
        x_temp=x_knight-2
        y_temp=y_knight+1

        if (not(x_temp>board_size or y_temp > board_size) and x_temp>0 and y_temp>0):          
            if((x_temp,y_temp) in moves):
                if(moves[(x_temp,y_temp)]>counter+1):
                    moves[(x_temp,y_temp)]=counter+1
                    calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)
            else:
                moves[(x_temp,y_temp)]=counter+1
                calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)

        # Work on side bottom right
        x_temp=x_knight+2
        y_temp=y_knight-1

        if (not(x_temp>board_size or y_temp > board_size) and x_temp>0 and y_temp>0):       
            if((x_temp,y_temp) in moves):
                if(moves[(x_temp,y_temp)]>counter+1):
                    moves[(x_temp,y_temp)]=counter+1
                    calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)
            else:
                moves[(x_temp,y_temp)]=counter+1
                calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)

        # Work on side bottom left
        x_temp=x_knight-2
        y_temp=y_knight-1

        if (not(x_temp>board_size or y_temp > board_size) and x_temp>0 and y_temp>0):           
            if((x_temp,y_temp) in moves):
                if(moves[(x_temp,y_temp)]>counter+1):
                    moves[(x_temp,y_temp)]=counter+1
                    calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)
            else:
                moves[(x_temp,y_temp)]=counter+1
                calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)

        # Work on bottom right
        x_temp=x_knight+1
        y_temp=y_knight-2

        if (not(x_temp>board_size or y_temp > board_size) and x_temp>0 and y_temp>0):          
            if((x_temp,y_temp) in moves):
                if(moves[(x_temp,y_temp)]>counter+1):
                    moves[(x_temp,y_temp)]=counter+1
                    calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)
            else:
                moves[(x_temp,y_temp)]=counter+1
                calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)

        # Work on bottom left
        x_temp=x_knight-1
        y_temp=y_knight-2

        if (not(x_temp>board_size or y_temp > board_size) and x_temp>0 and y_temp>0):          
            if((x_temp,y_temp) in moves):
                if(moves[(x_temp,y_temp)]>counter+1):
                    moves[(x_temp,y_temp)]=counter+1
                    calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)
            else:
                moves[(x_temp,y_temp)]=counter+1
                calculateMoves(x_target,y_target,x_temp,y_temp,board_size,counter+1)
        
        


calculateMoves(15,20,5,7,20,0)
#calculateMoves(1,1,4,5,6,0)
print(results)
print(min(results))
print("--- %s seconds ---" % (time.time() - start_time))
# if __name__=='__main__':
#     #print(t)    
#     t = input()
#     for i in range(int(t)):
#         results=[]
#         moves={}
#         size = int(input())
#         arr = list(map(int, input().strip().split()))
#         x_knight=arr[0]
#         y_knight=arr[1]
#         target = list(map(int, input().strip().split()))
#         x_target=target[0]
#         y_target=target[1]
#         calculateMoves(x_target,y_target,x_knight,y_knight,size,0)
#         if(len(results)==0):
#             print(1)
#         else:
#             print(min(results))
#         print()