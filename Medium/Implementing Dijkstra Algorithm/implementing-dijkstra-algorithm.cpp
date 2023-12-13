//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
	public:
	//Function to find the shortest distance of all the vertices
    //from the source vertex S.
    vector <int> dijkstra(int V, vector<vector<int>> adj[], int S)
    {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        vector<int> distance(V , 1e9);
        distance[S] = 0;
        minHeap.push({0 , S});
        
        while(!minHeap.empty()){
            pair<int, int> p = minHeap.top();
            minHeap.pop();
            
            int d = p.first;
            int node = p.second;
            
            for(auto it : adj[node]){
                int neighbour = it[0];
                int edgewEIGHT = it[1];
                
                int newD = d + edgewEIGHT;
                if(newD < distance[neighbour]){
                    // found better distance
                    minHeap.push({ newD , neighbour});
                    distance[neighbour] = newD;
                }
            }
        }
        
        return distance;
    }
        // Code here
    //     priority_queue<pair<int,int>,vector<pair<int,int>>,
    //     greater<pair<int,int>>>q;
    //     vector<int> dist(V);
    //     for(int i=0;i<V;i++){
    //         dist[i]=1e9;
    //     }
    //     dist[S]=0;
    //     q.push({0,S});
    //     while(!q.empty()){
    //         int node=q.top().first;
    //         int dis=q.top().second;
    //         q.pop();
    //         for(auto it:adj[node]){
    //             if(dis+it[1]<dist[it[0]]){
    //                 dist[it[0]]=dis+it[1];
    //                 q.push({dist[it[0]],it[0]});
    //             }
    //         }
    //     }
    //     for(int i=0;i<V;i++){
    //         if (dist[i]==1e9){
    //             dist[i]=0;
    //         }
    //     }
    //     return dist;
    // }
};


//{ Driver Code Starts.


int main()
{
    int t;
    cin >> t;
    while (t--) {
        int V, E;
        cin >> V >> E;
        vector<vector<int>> adj[V];
        int i=0;
        while (i++<E) {
            int u, v, w;
            cin >> u >> v >> w;
            vector<int> t1,t2;
            t1.push_back(v);
            t1.push_back(w);
            adj[u].push_back(t1);
            t2.push_back(u);
            t2.push_back(w);
            adj[v].push_back(t2);
        }
        int S;
        cin>>S;
        
        Solution obj;
    	vector<int> res = obj.dijkstra(V, adj, S);
    	
    	for(int i=0; i<V; i++)
    	    cout<<res[i]<<" ";
    	cout<<endl;
    }

    return 0;
}


// } Driver Code Ends