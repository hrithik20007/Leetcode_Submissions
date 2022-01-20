/*
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city 
b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly 
connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
*/








/*
Logic:
We use BFS to mark all the nodes in a connected graph as visited. The number of times we encounter an unvisited node,
means it is a part of a new unconnected component.
*/

class Solution {
public:
    void bfs(int source, vector<vector<int>> list, vector<bool> &vis){
        vis[source]=true;
        queue<int> q;
        q.push(source);

        while(!q.empty()){
            int curr=q.front();
            q.pop();
            for(auto it: list[curr]){
                if(vis[it]!=true){
                    q.push(it);
                    vis[it]=true;
                }
            }
        }
        
        return;
    }
    
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n=isConnected.size();
        vector<vector<int>> list(n,vector<int> ());
        vector<bool> vis(n,false);
        
        int i,j;
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                if(isConnected[i][j]==1 && i!=j){
                    list[i].push_back(j);
                    list[j].push_back(i);
                }
            }
        }
        
        int r=0;
        for(i=0;i<n;i++){
            if(vis[i]!=true){
                r+=1;
                bfs(i,list,vis);
            }
        }
        
        return r;
    }
};