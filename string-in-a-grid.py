def print_string_in_a_grid(arr,dim,target):
    grid=[];
    for i in range(dim[0]):
        start_row=i*dim[1];
        end_column=start_row+dim[1];
        grid.append(arr[start_row:end_column]);
    
    print grid
    is_match=False
    output=[]
    target_length=len(target);
    for i in range(0,dim[0]):
        for j in range(0,dim[1]):
            
            # Parse horizontal right
            if target_length<=dim[1]-j:
                temp_col_index=j;
                index=0;
                for col_index in range(temp_col_index,temp_col_index+target_length):
                    if target[index]!=grid[i][col_index]:
                        break;
                    index=index+1;
                
                if target_length==index:
                    is_match=True;
                    #print('{0} {1},'.format(i,j))  
                    output.append('{0} {1},'.format(i,j));
                    continue;
            
            # Parse horizontal left
            if target_length<=j+1:
                temp_col_index=j;
                index=0;
                for col_index in range(temp_col_index,temp_col_index-target_length,-1):
                    if target[index]!=grid[i][col_index]:
                        break;
                    index=index+1;
                
                if target_length==index:
                    is_match=True;
                    #print('{0} {1},'.format(i,j))  
                    output.append('{0} {1},'.format(i,j));
            
            # Parse vertical bottom
            if target_length<=dim[0]-i:
                temp_row_index=i;
                index=0;
                for row_index in range(temp_row_index,temp_row_index+target_length):
                    if target[index]!=grid[row_index][j]:
                        break;
                    index=index+1;
            
                if target_length==index:
                    is_match=True;
                    #print('{0} {1},'.format(i,j))  
                    output.append('{0} {1},'.format(i,j));

            # Parse vertical top
            if target_length<=i+1:
                temp_row_index=i;
                index=0;
                for row_index in range(temp_row_index,temp_row_index-target_length,-1):
                    if target[index]!=grid[row_index][j]:
                        break;
                    index=index+1;
            
                if target_length==index:
                    is_match=True;
                    #print('{0} {1},'.format(i,j))  
                    output.append('{0} {1},'.format(i,j));
            
            # Parse diagnol bottom right
            if target_length <= dim[0]-i and target_length <= dim[1]-j:
                temp_row_index=i;
                temp_col_index=j;
                index=0;
                for t_index in range(0,target_length):
                    if target[index]!=grid[i+t_index][j+t_index]:
                        break;
                    index=index+1;
                if target_length==index:
                    is_match=True;
                    #print('{0} {1},'.format(i,j))  
                    output.append('{0} {1},'.format(i,j));

            # Parse diagnol bottom left
            if target_length <= dim[0]-i and target_length <= j+1:
                temp_row_index=i;
                temp_col_index=j;
                index=0;
                for t_index in range(0,target_length):
                    if target[index]!=grid[i+t_index][j-t_index]:
                        break;
                    index=index+1;
                if target_length==index:
                    is_match=True;
                    #print('{0} {1},'.format(i,j))  
                    output.append('{0} {1},'.format(i,j));

            # Parse diagnol top right            
            if target_length <= i+1 and target_length <= dim[1]-j:
                temp_row_index=i;
                temp_col_index=j;
                index=0;
                for t_index in range(0,target_length):
                    if target[index]!=grid[i-t_index][j+t_index]:
                        break;
                    index=index+1;
                if target_length==index:
                    is_match=True;
                    #print('{0} {1},'.format(i,j))  
                    output.append('{0} {1},'.format(i,j));
            
            # Parse diagnol bottom left
            if target_length <= i+1 and target_length <= j+1:
                temp_row_index=i;
                temp_col_index=j;
                index=0;
                for t_index in range(0,target_length):
                    if target[index]!=grid[i-t_index][j-t_index]:
                        break;
                    index=index+1;
                if target_length==index:
                    is_match=True;
                    #print('{0} {1},'.format(i,j))  
                    output.append('{0} {1},'.format(i,j));

    if len(output)>0:
        print ' '.join(output);
    else:
        print '-1'

arr=['a','b','c','d','e','f','g','h','i','j','k','l'];
dim=[3,4]
target='a'
print_string_in_a_grid(arr,dim,target)
# if __name__=='__main__':
#     #print(t)
#     t = input()
#     for i in range(int(t)):        
#         dim = list(map(int, input().strip().split()))
#         arr = input().strip().replace(' ','')
#         target=input()
        
#         print_string_in_a_grid(arr,dim,target)
        