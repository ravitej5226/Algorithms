def PrintLeafNodes(arr,count):
    spanCount=[]
    for i in range(count):
        if(i*2+1>count-1 and i*2+2>count-1):
            spanCount.append(arr[i])
    for i in range(len(spanCount)):
        print(spanCount.pop(0),end=' ')



if __name__=='__main__':
    #print(t)
    t = input()
    for i in range(int(t)):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        PrintLeafNodes(arr,n)
        print()