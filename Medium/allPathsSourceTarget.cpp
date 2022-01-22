/*
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 
and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge 
from node i to node graph[i][j]).

Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
*/







/*
Logic:
Solved via BFS. A queue is used to store all temporary vectors. When a vector is popped from the queue, we chack whether
the last element in the vector is the (n-1)th node. If it is, we push the vector into the answer vector 'ans'.
*/

class Solution {
public:
    vector<vector<int>> ans;
    /*
    DFS Approach
    
    
    void dfs(int node,vector<vector<int>> graph,vector<int> l){
        l.push_back(node);
        if(node==graph.size()-1){
            ans.push_back(l);
            return;
        }
        if(graph[node].size()==0)
            return;
        
        for(auto it:graph[node])
            dfs(it,graph,l);
        
        return;
    }
    */
    void bfs(int node,vector<vector<int>> graph){
        queue<vector<int>> q;
        vector<int> l;
        l.push_back(node);
        q.push(l);
        
        while(!q.empty()){
            vector<int> l1=q.front();
            q.pop();
            int back=l1.back();
            if(back==graph.size()-1)
                ans.push_back(l1);

            for(auto it:graph[back]){           //Appending the individual adjacent nodes to the current temporary vector
                l1.push_back(it);
                q.push(l1);
                l1.pop_back();
            }
        }
        
        return;
    }
    
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int n=graph.size();
        bfs(0,graph);
        
        return ans;
    }
};