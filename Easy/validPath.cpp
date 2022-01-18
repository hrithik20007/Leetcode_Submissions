/*
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in 
the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge 
between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
You want to determine if there is a valid path that exists from vertex source to vertex destination.
Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, 
or false otherwise.

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Example 2:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
*/






/*
Logic:

We use a global boolean variable path (initialised as false) which deteremines whether a path between the source and 
destination exists or not. We use BFS to reach see whether the node can be reached (DFS is too slow and gives us TLE). If 
it can be reached, we change path to true and return. At the end, we return path.
*/
class Solution {
public:
    bool path=false;
    
    void bfs(int source,int destination,vector<vector<int>> list,vector<bool> &vis){
        queue<int> q;
        vis[source]=true;
        
        q.push(source);
        while(q.empty()==false && path==false){
            int node=q.front();
            q.pop();
    
            for(auto it:list[node]){
                if(it==destination){
                    path=true;
                    break;
                }
                if(vis[it]!=true){
                    vis[it]=true;
                    q.push(it);
                }
            }   
        }
        
        return;
    }
    
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        if(n==1 && source==0 && destination==0)
            return true;
        
        vector<vector<int>> list(n,vector<int>());
        vector<bool> vis(n,false);
        
        for(int i=0;i<edges.size();i++){
            list[edges[i][0]].push_back(edges[i][1]);
            list[edges[i][1]].push_back(edges[i][0]);
        }
        
        bfs(source,destination,list,vis);
        return path;
    }
};