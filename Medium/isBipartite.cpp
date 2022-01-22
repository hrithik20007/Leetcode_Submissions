/*
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, 
where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an 
undirected edge between node u and node v. The graph has the following properties:
There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph 
connects a node in set A and a node in set B.
Return true if and only if it is bipartite.

Example 1:
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

Example 2:
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
*/






/*
Logic:
Solved using DFS. Basic logic is that I colour the starting node as red (1 for red, 0 for white and -1 for uncoloured), 
and its adjacent nodes the opposite colour and their nodes the opposite colour and so on. If I encounter a visited node,
I check whether the colour of the visited node is the same as the one I was about to fill it up with. If not, that means
two adjacent nodes are having the same colour which shouldn't be possible in a bipartite graph. So we return false; 
otherwise return true. This approach is also called Graph-Colouring.
*/

class Solution {
public:
    bool check(int node, vector<vector<int>> graph, vector<int> &color, vector<int> &vis, int col){
        if(vis[node]==true){
            if(color[node]==col)
                return true;
            return false;
        }
        
        vis[node]=true;
        color[node]=col;
        
        for(auto it: graph[node]){
            if(check(it,graph,color,vis,col xor 1)==false)
                return false;
        }
        
        return true;
    }
    
    bool isBipartite(vector<vector<int>>& graph) {
        int n=graph.size();
        vector<int> vis(n,false);
        vector<int> color(n,-1);
        
        for(int i=0;i<n;i++){
            if(vis[i]!=true){
                if(check(i,graph,color,vis,1)==false)
                    return false;
            }
        }
        
        return true;
    }
};


/*
A BFS approach



bool helper(vector<vector<int>>& graph,vector<bool>& visited,vector<int>& color,int start_v) {
    queue<int>q;
    q.push(start_v);
    visited[start_v] = true;
    color[start_v] = 0;// white
    while(!q.empty()){
        int top = q.front();
        q.pop();
        
        for(auto v : graph[top]) {
            if(!visited[v]) {
                visited[v] = true;
                color[v] = !(color[top]); // opposite color
                q.push(v);
            }
            else if(color[v] == color[top]) {
                return false;
            }
        }
    }
    return true;
*/