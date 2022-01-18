/*
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array 
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course 
ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it 
is impossible.
*/






/*
Logic:
We are essentially checking if there is a cycle present in the directed graph. If yes, then all the courses cannot be 
finished and we return false, while vice-versa for non-cyclic. Now, we check for a cycle via BFS.
The main logic is that all indegrees (path coming in) to a node which is not part of a cycle, should be a from a node
which has 0 indegree (like a starting node). If there is a cycle present, then it is mandatory that at least one of its
incoming path is a part of a cycle (thus all the nodes in that cycle will not have 0 indegree). 
We only push a node into the queue if all of its indegrees have a starting point from a node with 0 indegree. If by the
end, the queue has held all the nodes at one point or the other, that means none of nodes were part of a cycle. So we
return true, otherwise false. 
*/

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        int n=numCourses;
        vector<vector<int>> list(n,vector<int>());
        vector<int> indeg(n,0);
        
        int i;
        int node;
        int n1=0;
        for(i=0;i<prerequisites.size();i++){
            int u=prerequisites[i][1];
            int v=prerequisites[i][0];
            list[u].push_back(v);
            indeg[v]+=1;
        }
        
        queue<int> q;
        for(i=0;i<n;i++){
            if(indeg[i]==0)
                q.push(i);
        }
        
        while(!q.empty()){
            node=q.front();
            q.pop();
            n1+=1;
            
            for(auto it:list[node]){
                indeg[it]-=1;
                if(indeg[it]==0)
                    q.push(it);
            }
        }
        
        if(n1==n)
            return true;
        else
            return false;
        
        
        
        
    /*
    Gives TLE (Uses DFS)
    
    
    bool cycledetect(int node, vector<vector<int>> list, vector<bool> &vis, vector<bool> &st){
        if(vis[node]==true)
            return false;
        
        vis[node]=true;
        st[node]=true;
        for(auto it:list[node]){
            if(st[it]==true)
                return true;
            if(vis[it]==false && cycledetect(it,list,vis,st))
                return true;
        }
        st[node]=false;
        return false;
    }
    
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        int n=numCourses;
        vector<vector<int>> list(n,vector<int>());
        vector<bool> vis(n,false);
        vector<bool> st(n,false);
        
        int i;
        for(i=0;i<prerequisites.size();i++){
            int u=prerequisites[i][1];
            int v=prerequisites[i][0];
            list[u].push_back(v);
        }
        
        bool cycle=false;
        for(i=0;i<n;i++){
            if(vis[i]==false && cycledetect(i,list,vis,st))
                cycle=true;
        }
        
        if(cycle)
            return false;
        else
            return true;
    */
    }
};