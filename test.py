def print_string_in_a_grid(arr,dim,target):
    grid=[];
    for i in range(dim[0]):
        start_row=i*dim[1];
        end_column=start_row+dim[1];
        grid.append(arr[start_row:end_column]);
    
    is_match=False
    for i in range(dim[0]):
        for j in range(dim[1]):
            
            # Parse horizontal right
            if(len(target)<=dim[1]-j):
                temp_column=j
                target_index=0
                for temp_column in range(j,dim[1]):
                    if(target[target_index]!=grid[i][temp_column]):
                        break
                    target_index=target_index+1            
            
                if(len(target)==target_index):
                    is_match=True
                    print('{0} {1},'.format(i,j))


            # Parse horizontal left
            if(len(target)<=j+1):
                temp_column=j
                target_index=0
                for temp_column in range(j,-1,-1):
                    if(target[target_index]!=grid[i][temp_column]):
                        break
                    target_index=target_index+1            
            
                if(len(target)==target_index):
                    is_match=True
                    print('{0} {1},'.format(i,j))
            
            # Parse vertical top
            if(len(target)<=i+1):
                temp_row=i
                target_index=0
                for temp_row in range(i,-1,-1):
                    if(target[target_index]!=grid[temp_row][j]):
                        break
                    target_index=target_index+1            
            
                if(len(target)==target_index):
                    is_match=True
                    print('{0} {1},'.format(i,j))
            
            # Parse vertical bottom
            if(len(target)<=dim[0]-i):
                temp_row=i
                target_index=0
                for temp_row in range(i,dim[0]):
                    if(target[target_index]!=grid[temp_row][j]):
                        break
                    target_index=target_index+1            
            
                if(len(target)==target_index):
                    is_match=True
                    print('{0} {1},'.format(i,j))

            # Parse diagnol top right
            target_index=0
            for temp_row,temp_column in zip(range(i,-1,-1),range(j,dim[1])):                        
                if(target[target_index]!=grid[temp_row][temp_column]):
                    break
                target_index=target_index+1            
            
            if(len(target)==target_index):
                is_match=True
                print('{0} {1},'.format(i,j))
            
            # Parse diagnol top left
            target_index=0
            for temp_row,temp_column in zip(range(i,-1,-1),range(j,-1,-1)):                        
                if(target[target_index]!=grid[temp_row][temp_column]):
                    break
                target_index=target_index+1            
            
            if(len(target)==target_index):
                is_match=True
                print('{0} {1},'.format(i,j))
            
            # Parse diagnol bottom left
            target_index=0
            for temp_row,temp_column in zip(range(i,dim[i]),range(j,-1,-1)):                        
                if(target[target_index]!=grid[temp_row][temp_column]):
                    break
                target_index=target_index+1            
            
            if(len(target)==target_index):
                is_match=True
                print('{0} {1},'.format(i,j))
            
            # Parse diagnol bottom right
            target_index=0
            for temp_row,temp_column in zip(range(i,dim[i]),range(j,dim[j])):                        
                if(target[target_index]!=grid[temp_row][temp_column]):
                    break
                target_index=target_index+1            
            
            if(len(target)==target_index):
                is_match=True
                print('{0} {1},'.format(i,j))
            
    if(is_match==False):
        print(-1)


if __name__=='__main__':
    #print(t)
    t = input()
    for i in range(int(t)):        
        dim = list(map(int, input().strip().split()))
        arr = input().strip().replace(' ','')
        target=input()
        
        print_string_in_a_grid(arr,dim,target)
        