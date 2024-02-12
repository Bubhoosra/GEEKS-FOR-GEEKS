#User function Template for python3

class Solution:
    def sequence(self, n):
        i=1
        j=1
        result=0
        for i in range(1,n+1):
            ans=1
            while(i>0):
                ans*=j
                j+=1
                i-=1
            result+=ans
        return result%((10**9)+7)
                
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends