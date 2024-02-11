#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        prev=0
        a=[0]*n
        a[0]=0
        d={}
        d[0]=1
        for i in range(1,n):
            x=a[i-1]-i
            if x<0 or x in d:
                x=a[i-1]+i
            a[i]=x
            d[x]=1
        return a
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends