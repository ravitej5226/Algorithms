# Given an input stream of n integers the task is to insert integers to stream and print the kth largest element in the stream at each insertion.

# Example:

# Input:
# stream[] = {10, 20, 11, 70, 50, 40, 100, 5, ...}
# k = 3

# Output:    {-1,   -1, 10, 11, 20, 40, 50,  50, ...}

# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two lines. The first line of each test case contains two space separated integers k and n . Then in the next line are n space separated values of the array.

# Output:
# For each test case in a new line print the space separated values denoting the kth largest element at each insertion, if the kth largest element at a particular insertion in the stream doesn't exist print -1.

# Constraints:
# 1<=T<=100
# 1<=n,k<=1000
# 1<=stream[]<=100000

# Example:
# Input:
# 2
# 4 6
# 1 2 3 4 5 6
# 1 2
# 3 4 

# Output:
# -1 -1 -1 1 2 3
# 3 4 
class minHeap:
    def __init__(self):
        self.heapList=[0];
        self.heapSize=0;
    
    def insert(self,item):
        # Append to end of array
        self.heapList.append(item);

        # Increment size of heap
        self.heapSize=self.heapSize+1;

        # Percolate the item up till heap size is restored
        self.percolateUp(self.heapSize);
    
    def percolateUp(self,index):
        # while item at index is less than parent
        while index//2>0:
            if self.heapList[index]<self.heapList[index//2]:
                # swap item at index with parent
                self.heapList[index]=self.heapList[index]+self.heapList[index//2];
                self.heapList[index//2]=self.heapList[index]-self.heapList[index//2];
                self.heapList[index]=self.heapList[index]-self.heapList[index//2];
                
            # Continue till item at index is greater than parent
            index=index//2;
    
    def deleteMin(self):
        if self.heapSize==1:
            self.heapSize=0;
            self.heapList.pop();
        if self.heapSize>1:
            # get the element at root (index: 1)        
            minElement = self.heapList[1];

            # Replace the root with last element in the array
            self.heapList[1]=self.heapList[self.heapSize]
            self.heapList.pop();

            # Reduce the size of heap
            self.heapSize=self.heapSize-1;

            # Percolate down to maintain the min heap
            self.percolateDown(1);                        
    
    def percolateDown(self,index):
        while (index * 2) <= self.heapSize:
            # Get the index of min child
            minChildIndex=self.getMinChildIndex(index);

            # While min child index is less than root
            if self.heapList[minChildIndex]<self.heapList[index]:
                # swap the parent and child
                self.heapList[index]=self.heapList[index]+self.heapList[minChildIndex];
                self.heapList[minChildIndex]=self.heapList[index]-self.heapList[minChildIndex];
                self.heapList[index]=self.heapList[index]-self.heapList[minChildIndex];

            # Set index to index of min child
            index=minChildIndex;
            
    
    def getMinChildIndex(self,i):
        if i*2+1>self.heapSize:
            return i*2;
        else:
            if self.heapList[i*2]>self.heapList[i*2+1]:
                return i*2+1;
            else:
                return i*2;
    
    def getMinElement(self):
        if self.heapSize>0:
            return self.heapList[1];
        else :
            return -1;

def printKthLargestElement(arr,k,count):
    heap=minHeap();
    output=[];

    # Loop each element in array
    for i in range(0,count):
        if i==49:
            print heap.heapList
        # If the heap size is less than k
        # Add to heap and print -1
        if heap.heapSize<k-1:
            heap.insert(arr[i]);
            output.append(-1);
        elif heap.heapSize==k-1:
            heap.insert(arr[i]);
            output.append(heap.getMinElement());
        else:
            # If heap is greater than k,        
            # If current element is greater than k, 
            if arr[i]>heap.getMinElement():
                # delete min and print kth largest element
                heap.deleteMin();
                heap.insert(arr[i]);
                output.append(heap.getMinElement());
            else:
                # Else print kth largest element
                output.append(heap.getMinElement());

    # for i in range(len(output)):
        #print(output.pop(0),end=' ')
    print(output)

printKthLargestElement([778,916,794,336,387,493,650,422,363,28,691,60,764,927,541,427,173,737,212,369,568,430,783,531,863,124,68,136,930,803,23,59,70,168,394,457,12,43,230,374,422,920,785,538,199,325,316,371,414,527,92,981,957,874,863,171,997,282,306,926,85,328,337,506,847,730,314,858,125,896,583,546,815,368,435,365,44,751,88,809,277,179,789,585],47,84)
# if __name__=='__main__':
#     #print(t)
#     t = input()
#     for i in range(int(t)):
#         n = list(map(int, input().strip().split()))
#         k=n[0]
#         count=n[1]
#         arr = list(map(int, input().strip().split()))
#         printKthLargestElement(arr,k,count)
#         print()