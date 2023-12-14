//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  private:
     
  public:
    int shortestPath(vector<vector<int>> &grid, pair<int, int> source,
                     pair<int, int> destination) {
    if (destination==source)  return 0;
    int n=grid.size();
    int m=grid[0].size();
    int row[]={-1,0,+1,0};
    int col[]={0,+1,0,-1};
    vector<vector<int>>vis(n,vector<int>(m,0));
    queue<pair<pair<int,int>,int>>q;
    q.push({{source.first,source.second},0});
    while(!q.empty()){
        auto it=q.front();
        q.pop();
        pair<int,int>index=it.first;
        int ith=index.first;
        int jth=index.second;
        int dis=it.second;
        if(index==destination)  return dis;
        for(int i=0;i<4;i++){
            int newith=ith+row[i];
            int newjth=jth+col[i];
            if(newith<n && newjth<m && newith>=0 && newjth>=0
            && grid[newith][newjth]==1 && vis[newith][newjth]==0){
                vis[newith][newjth]=1;
                q.push({{newith,newjth},dis+1});
            }
            
        }
    }
    return -1;
        // code here
    }
};


//{ Driver Code Starts.
int main() {

    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> grid(n, vector<int>(m));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> grid[i][j];
            }
        }

        pair<int, int> source, destination;
        cin >> source.first >> source.second;
        cin >> destination.first >> destination.second;
        Solution obj;
        cout << obj.shortestPath(grid, source, destination) << endl;
    }
}

// } Driver Code Ends