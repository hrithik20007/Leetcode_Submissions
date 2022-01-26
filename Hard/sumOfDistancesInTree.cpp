/*
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes 
ai and bi in the tree.
Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all 
other nodes.

Example 1:
Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

Example 2:
Input: n = 1, edges = []
Output: [0]

Example 3:
Input: n = 2, edges = [[1,0]]
Output: [1,1]
*/







/*
Logic: Look at the official Leetcode solution for better understanding.
Consider the graph given in e.g. => 0-1, 0-2, 2-3, 3-4, 4-5. Draw this in your notes.

Hint 1:
Now try to find recursion between the nodes.

Hint 2:
N[i] = number of nodes in subtree of i(including i)
P[i] = Sum of path from node i to its descendants.
S[i] = Sum of path from node i to all other nodes = answer for node i
If you are given the above info, can you write recursion for S[i] and P[i]?

Hint 3:
Consider this recursion:
P[i] = Sum(P[j] + N[j]) s.t. node j is child of node i
N[i] = Sum(N[j])
S[0] = P[0]
Can you think of recussion for S[i] now?

Hint 4:
S[i] = S[parent[i]] + (n-N[i]) - N[i]=> Why does this recursion work? See from the graph you drawed from notes

Explanation:
Explaining why S[i] = S[parent[i]] + (n-N[i]) - N[i] works. Lets see it component by component.
For clarity assume p = parent[i] = 2 and i = 3
We want sum from node 3. To get that, you just need to focus on correcting the edge from i and p because all other things 
are correctly calculated by S[p]. What is wrong with i and p edge? S[p] calculates from 2->3 edge and its subtree 
sum(i.e. P[3]) but for S[i] we need to calculate from 3->2.
So the number of times edge 2-3 is calculated in S[p] != the number of time edge 2-3 is considered in S[i]. For all other 
edges the value is equal.
n-N[i] = Number of times the edge 2-3 should be considered for S[i]
N[i] = Number of times the edge 2-3 is considered in S[p]

So to correct the value we addn-N[i] and subtract N[i] from S[p] to get S[i].
*/

class Solution {
public:
    int n;
    vector<vector<int>> adj;
    vector<int> size;
    vector<int> dist;    
    vector<int> ans; 
    
    void dfs2(int currNode, int parent){
        for(auto adjNode : adj[currNode]){
            if(adjNode != parent){
                ans[adjNode] = ans[currNode] + ( n-size[adjNode] ) - (size[adjNode]);
                dfs2(adjNode, currNode);
            }
        }
        
        return; 
    }
    
    void dfs1(int currNode, int parent){
        size[currNode] = 1;
        
        for(auto adjNode : adj[currNode]){    
            if(adjNode != parent){
                dfs1(adjNode, currNode);
                dist[currNode] += dist[adjNode] + size[adjNode]; 
                size[currNode] += size[adjNode];
            }
        }
        return;
    }
    
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        this->n = n;
        adj.resize(n);
        size.resize(n,0);
        dist.resize(n,0);
        ans.resize(n,0);
        
        for(auto e :  edges){
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        
        dfs1(0,-1);
        ans[0] = dist[0];
        dfs2(0, -1);
        
        return ans; 
        
    
    /*
    Same as above, but dosen't work. Don't know why.
    
    
    int n;
    int root;
    vector<vector<int>> list;
    vector<int> ans;
    vector<int> dis;
    vector<int> size;
    
    void dfs1(int node,int parent){
        size[node]=1;
        
        for(auto it:list[node]){
            if(it!=parent){
                dfs1(it,node);
                dis[node]+=dis[it]+size[it];
                size[node]+=size[it];
            }
        }
            
        return;
    }
    
    void dfs2(int node,int parent){
        for(auto it:list[node]){
            if(it!=parent){
                ans[it]=ans[node]+(n-size[it])-size[it];
                dfs2(it,node);
            }
        }
        
        return;
    }
    
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges){    
        this->n=n;
        this->root=0;
        this->list.resize(n);
        this->ans.resize(n,0);
        this->dis.resize(n,0);
        this->size.resize(n,0);
        
        int i;
        for(i=0;i<n;i++){
            int u=edges[i][0];
            int v=edges[i][1];
            list[u].push_back(v);
            list[v].push_back(u);
        }
        
        dfs1(root,-1);
        ans[root]=dis[root];
        dfs2(root,-1);
        
        return ans;
    */
    }
};