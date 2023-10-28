#User function Template for python3

class Solution:
    def dfs(self,node,visited,d):
        visited[node]=1
        for i in d[node]:
            if visited[i]==0:
               self.dfs(i,visited,d)
        
    def numProvinces(self, adj, V):
        # print(adj)
        d={}
        for i in range(V):
            d[i]=[]
        for i in range(V):
            for j in range(V):
                if i!=j and adj[i][j]==1:
                    
                    d[i].append(j)
        visited={}
        for i in range(V):
            visited[i]=0
        c=0
        for i in range(V):
            if visited[i]==0:
                c+=1
                self.dfs(i,visited,d)
                
                    
                    
                    
        # print(d)
                
        
                    
                
            
        return c
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends