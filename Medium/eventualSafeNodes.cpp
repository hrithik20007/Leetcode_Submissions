/*
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D 
integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i 
to each node in graph[i].
A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that 
node leads to a terminal node.
Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Example 1:
Illustration of graph
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

Example 2:
Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
*/







/*
Logic:
Solved using the logic of Topological sort, but not exactly. In TS, we put the nodes with 0 indegree first and so on. Here,
we do the opposite, putting the ones with 0 outdegree first. Then we track back to all the nodes which are its parent/
ancestor, meaning a path should exist from the parent to the leaf. Theoritically, all nodes are safe nodes unless it is a 
part of a cycle.
*/

class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int i,j,n=graph.size();
        vector<int> ans;                        //Answer vector
        vector<int> outdeg(n);
        vector<vector<int>> g(n,vector<int>());
        queue<int> q;
        
        for(i=0;i<n;i++){
            outdeg[i]=graph[i].size();          //Outdegree of a node
            for(j=0;j<graph[i].size();j++)
                g[graph[i][j]].push_back(i);    //The nodes whose edges are incoming to a current node 
        }
        
        for(i=0;i<outdeg.size();i++){           //Nodes with 0 outdegree are pushed first
            if(outdeg[i]==0){
                q.push(i);
                ans.push_back(i);
            }
        }
        
        while(!q.empty()){
            int v=q.front();
            q.pop();
            
            for(auto it:g[v]){
                outdeg[it]-=1;
                if(outdeg[it]==0){ 
                    q.push(it);
                    ans.push_back(it);
                }
            }
        }
    
    
        sort(ans.begin(),ans.end());
        return ans;
    
    /*
    Gives TLE (DFS with Memoization)




    bool dfs(int node,vector<vector<int>> graph,vector<bool> &vis, map<int,bool> &mp){
        if(mp[node])
            return mp[node];
        if(graph[node].size()==0){
            mp[node]=true;
            vis[node]=true;
            return true;
        }
        
        vis[node]=true;
        
        for(auto it:graph[node]){
            if(vis[it]!=true){
                if(dfs(it,graph,vis,mp)==false)
                    return mp[node]=false;
            }
            else if(vis[it]==true && mp[it]!=true)
                return mp[node]=false;
        }
        
        return mp[node]=true;
    }
    
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n=graph.size();
        vector<bool> vis(n,false);
        map<int,bool> mp;
        
        vector<int> s;
        for(int i=0;i<n;i++){
            if(dfs(i,graph,vis,mp))
                s.push_back(i);
        }

        return s;
    */
    }
};