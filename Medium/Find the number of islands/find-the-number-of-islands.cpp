//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    // Function to find the number of islands.
    void bfs(int i,int j,vector<vector<int>>&visited, vector<vector<char>>&grid){
        visited[i][j]=1;
        queue<pair<int,int>>q;
        q.push({i,j});
        
        int n=grid.size();
        int m=grid[0].size();
        while(!q.empty()){
            int row=q.front().first;
            int col=q.front().second;
            q.pop();
            for(int nrow=-1 ;nrow<=1;nrow++){
                for(int ncol=-1;ncol<=1;ncol++){
                    int r=nrow+row;
                    int c=ncol+col;
                    if (r>=0 && r<n && c>=0 && c<m && 
                    grid[r][c]=='1' && !visited[r][c]){
                        visited[r][c]=1;
                        q.push({r,c});
                    }
                }
            }
            
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int n=grid.size();
        int m=grid[0].size();
        int c=0;
        vector<vector<int>>visited(n,vector<int>(m,0));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if (!visited[i][j] && grid[i][j]=='1'){
                    c++;
                    bfs(i,j,visited,grid);
                }
                
            }
        }
        return c;
        // Code here
    }
};

//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;
        vector<vector<char>> grid(n, vector<char>(m, '#'));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> grid[i][j];
            }
        }
        Solution obj;
        int ans = obj.numIslands(grid);
        cout << ans << '\n';
    }
    return 0;
}
// } Driver Code Ends