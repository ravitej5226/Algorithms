class Solution(object):
    def flatten_array(self,arr):
        if(type(arr)!=list):
            return [arr]
        else:
            result=[]
            for i in range(len(arr)):
                result = result + self.flatten_array(arr[i])
        return result
        
s=Solution()
print(s.flatten_array([1,2,[3,[4,5]]]))