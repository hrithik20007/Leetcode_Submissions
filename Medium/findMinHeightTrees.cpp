/*
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected 
graph without simple cycles is a tree.
Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that 
there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root.
When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum 
height (i.e. min(h))  are called minimum height trees (MHTs).
Return a list of all MHTs' root labels. You can return the answer in any order.
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
*/







/*
Logic:
We need to find the minimum height trees and return the roots of those trees. There can be atmost 2 trees with minimum height. So the result vector can have atmost 2 elements. Let's see how!

APPROACH :
For the graph with odd no. of nodes, only the node at the middle of the graph when made the root, will give a minimum 
height tree.
For the graph with even no. of nodes, both the middle nodes when made the root give a minimum height tree.
So, we need to start from the leaf nodes and find a way to approach the middle nodes, add them to the result vector and 
return the answer.
How do we do that?

We use Topological Sorting!
- We create an array called indegree which keeps the count of the no. of edges approaching each node in the tree.
- We start with the nodes having the minimum indegree (ie; indegree=1, i.e the leaf nodes) and we go on removing them i.e 
  decrementing the indegree of nodes that're connected to them, until we reach the middle nodes.
- So we can have only one root or at max two roots for minimum height depending on tree structure as explained above.
- For the implementation, we are going to use a BFS like approach.
- To begin with, all leaf node are pushed into the queue, then they are removed from the tree, next new leaf node is 
  pushed in the queue, this procedure keeps on going until we have only 1 or 2 node in our tree, which represent the result.

Time Complexity : O(V+E)
Space Complexity : O(V)
*/

class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        vector<int> indegree(n, 0), ans;
        
        for(auto e : edges){   
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
            indegree[e[0]]++;
            indegree[e[1]]++;
        }
        
        queue<int> q;
        for(int i=0; i<n;i++){
            if(indegree[i]==1){
                q.push(i);
                indegree[i]--;              //Only the indegree of the leaf nodes are deducted. Their outgoing edges are 
                                            //still present
            }
        } 
        
        while(!q.empty()){
            ans.clear();                    //ans vector is cleared after every iteration so as to hold the final one 
                                            //(or two) elements only
            int s=q.size(); 
            
            for(int i=0;i<s;i++){
                int curr=q.front(); q.pop();
                ans.push_back(curr);
                
                for(auto it:graph[curr]){
                    indegree[it]-=1;
                    if(indegree[it]==1){
                        q.push(it);
                    }
                }
            }
        }
            
        if(n==1) ans.push_back(0);
        return ans;
    
    
    /*
    Gives TLE
    
    
    
    
    //We do not use a visisted vector here as there is only one path from one vertex to another. So it is not possible to encounter a node during a DFS traversal, that has already been traversed before
    int dfs(int source,vector<vector<int>> list, bool &f){
        if(list[source].size()==1 && f==true)
            return 1;
        
        f=true;
        
        int maximum=INT_MIN;
        for(auto it:list[source]){
            if(it!=source){
                maximum=max(maximum,dfs(it,list,f));
            }
        }
        
        return maximum+1;
    }
    
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges){
        vector<vector<int>> list(n,vector<int>());
        map<int,int> mp;
        vector<int> ans;
        
        int i=0;
        for(i=0;i<n-1;i++){
            int u=edges[i][0];
            int v=edges[i][1];
            list[u].push_back(v);
            list[v].push_back(u);
        }
        
        int h,mh=INT_MAX;
        for(i=0;i<n;i++){
            h=1;
            bool f=false;
            if(list[i].size()!=0)
                h=dfs(i,list,f);
            mh=min(mh,h);
            mp[i]=h;
        }
        
        for(auto it:mp){
            if(it.second==mh)
                ans.push_back(it.first);
        }
        
        return ans;
    */
    }
};