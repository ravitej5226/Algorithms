import heapq
class Solution(object):
    def reorganizeString(self, s):
        ans=[]

        # Create a set with count
        heap=[(-s.count(x),x) for x in set(s)]

        # heapify the set
        heapq.heapify(heap)

        # If any character has count n+1/2, return empty string
        if any(-count>(len(s)+1)/2 for count,x in heap):
            return ''
        
        # Else while length of heap is greater than equal to 2
        while (len(heap)>=2):
            
            # Get top 2 elements
            top1,ch1=heapq.heappop(heap)
            top2,ch2=heapq.heappop(heap)

            # Append to answer
            ans.extend([ch1,ch2])

            # update the count and add it to heap again
            if(top1+1):
                heapq.heappush(heap,(top1+1,ch1))
            
            if(top2+1):
                heapq.heappush(heap,(top2+1,ch2))

        # Append the last character in the heap
        # return
        
        return "".join(ans) + (heap[0][1] if heap else '')

s=Solution()
print(s.reorganizeString('aab'))