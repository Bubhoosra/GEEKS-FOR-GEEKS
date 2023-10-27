#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self,l,adj,d,node):
        l.append(node)
        if node not in d:
            d[node]=1
        for i in adj[node]:
            if i not in d:
                self.dfs(l,adj,d,i)
    def dfsOfGraph(self, V, adj):
        d={}
        ans=[]
        for i in range(V):
            if i not in d:
                l=[]
                self.dfs(l,adj,d,i)
                for i in l:
                    ans.append(i)
        return ans
        
        # code here


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends