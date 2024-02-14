# User function Template for Python3

class Solution:
    def equalPartition(self, N, nums):
        s=sum(nums)
        n=len(nums)
        if n==1:
            return False
        if s%2:
            return False
        target=s//2
        dp=[]
        for i in range(n):
            l=[]
            for j in range(target+1):
                l.append(0)
            dp.append(l)
        if nums[0]<=target:
            dp[0][nums[0]]=True
        for i in range(n):
            dp[i][0]=True
        # print(dp)
        for i in range(1,n):
            for j in range(1,target+1):
                ntake=dp[i-1][j]
                take=False
                if(j>=nums[i]):
                    take=dp[i-1][j-nums[i]]
                dp[i][j]=take or ntake
        # print(dp)
        return dp[n-1][target]
        # code here


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends