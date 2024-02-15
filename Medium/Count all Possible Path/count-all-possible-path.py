#User function Template for python3
def dfs(i,adj,vis):
    vis[i]=1
    for j in adj[i]:
        if vis[j]==0:
            dfs(j,adj,vis)
class Solution:
	def isPossible(self, paths):
	    n=len(paths)
	    col=len(paths[0])
	    adj={}
	    for i in range(n):
	        adj[i]=[]
	    for i in range(n):
	        for j in range(col):
	            if paths[i][j]==1:
	                adj[i].append(j)
	        if len(adj[i])%2==1:
	            return 0
	    return 1
	   # \pend(l)
	    
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		paths = []
		for _ in range(n):
			cur = list(map(int, input().split()))
			paths.append(cur)
		obj = Solution()
		ans = obj.isPossible(paths)
		print(ans)

# } Driver Code Ends