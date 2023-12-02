//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution {
  private:
    void dfs(int node,unordered_map<int,list<int>>&um,int vis[]){
        vis[node]=1;
        for (auto i:um[node]){
            if(!vis[i]){
                dfs(i,um,vis);
            }
        }
    }
  public:
    int numProvinces(vector<vector<int>> adj, int V) {
        int n=adj.size();
        unordered_map<int,list<int>>um(n);
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if (i!=j && adj[i][j]==1){
                    um[i].push_back(j);
                    um[j].push_back(i);
                }
            }
            
        }
        int vis[n];
        for(int i=0;i<n;i++){
            vis[i]=0;
        }
        int c=0;
        for(int i=0;i<n;i++){
            if(!vis[i]){
                c++;
                dfs(i,um,vis);
            }
        }
        return c;
        // code here
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int V,x;
        cin>>V;
        
        vector<vector<int>> adj;
        
        for(int i=0; i<V; i++)
        {
            vector<int> temp;
            for(int j=0; j<V; j++)
            {
                cin>>x;
                temp.push_back(x);
            }
            adj.push_back(temp);
        }
        

        Solution ob;
        cout << ob.numProvinces(adj,V) << endl;
    }
    return 0;
}
// } Driver Code Ends