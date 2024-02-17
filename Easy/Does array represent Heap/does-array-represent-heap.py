
class Solution:
    def isMaxHeap(self,arr,n):
        m=arr[0]
        for i in range(n):
            if 2*i+1<n:
                if arr[2*i+1]>arr[i]:
                    return False
            if 2*i+2<n:
                if arr[2*i+2]>arr[i]:
                    return False
                
        
        return True
        
        # Your code goes here            



#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends