/*
There is a group of n people labeled from 0 to n - 1 where each person has a different amount of money and a different 
level of quietness.
You are given an array richer where richer[i] = [ai, bi] indicates that ai has more money than bi and an integer array 
quiet where quiet[i] is the quietness of the ith person. All the given data in richer are logically correct (i.e., the 
data will not lead you to a situation where x is richer than y and y is richer than x at the same time).
Return an integer array answer where answer[x] = y if y is the least quiet person (that is, the person y with the smallest 
value of quiet[y]) among all people who definitely have equal to or more money than the person x.

Example 1:
Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
Output: [5,5,2,5,4,5,6,7]
Explanation: 
answer[0] = 5.
Person 5 has more money than 3, which has more money than 1, which has more money than 0.
The only person who is quieter (has lower quiet[x]) is person 7, but it is not clear if they have more money than person 0.
answer[7] = 7.
Among all people that definitely have equal to or more money than person 7 (which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x]) is person 7.
The other answers can be filled out with similar reasoning.

Example 2:
Input: richer = [], quiet = [0]
Output: [0]
*/







/*
Logic:
Solved using DFS. The nodes at the end have no richer person than them, so we return them as y for the ans vector. For 
middle nodes, we trace a path to their respective adjacent nodes and find the minimum quiet node from them. The ans vector
also acts as a memoization dictionary.
*/

class Solution {
public:
    vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet) {
        int n = quiet.size();
        vector<vector<int>> graph(n);
        for(auto i : richer)
            graph[i[1]].push_back(i[0]);

        vector<bool> visited(n, false);
        vector<int> ans(n);
        for(int i = 0; i < n; i++)
            if(!visited[i])
                dfs(i, visited, ans, quiet, graph);

        return ans;
    }

    int dfs(int i, vector<bool> &visited, vector<int> &ans, vector<int> &quiet, vector<vector<int>> &graph)
    {
        if(visited[i])
            return ans[i];

        int tmp = i;
        for(auto j : graph[i])
        {
            int tmp2 = dfs(j, visited, ans, quiet, graph);
            if(quiet[tmp] > quiet[tmp2])
                tmp = tmp2;
        }

        visited[i] = true;
        return ans[i] = tmp;


    /*
    Same logic as above but gives TLE, don't know why
    
    
    int dfs(int node,vector<vector<int>> list,vector<bool> &vis,vector<int> &ans,vector<int> quiet){
        if(vis[node])
            return ans[node];
        
        //vis[node]=true;
        int tmp=node;
        for(auto it:list[node]){
            int tmp2=dfs(it,list,vis,ans,quiet);
            if(quiet[tmp]>quiet[tmp2])
                tmp=tmp2;
        }
        
        vis[node]=true;
        return ans[node]=tmp;
    }
    
    vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet) {
        int i;
        int n=quiet.size();
        vector<vector<int>> list(n);
        vector<int> ans(n);
        vector<bool> vis(n,false);
        
        for(auto it:richer)
            list[it[1]].push_back(it[0]);
        
        for(i=0;i<n;i++){
            if(vis[i]!=true)
                dfs(i,list,vis,ans,quiet);
        }
        
        return ans;
    */    

    /*
    Gives TLE
    
    
    map<int,int> mp;
    int bfs(int node, vector<vector<int>>list, vector<int> quiet){
        queue<int> q;
        vector<int> l;
        q.push(node);
        l.push_back(node);
        
        while(!q.empty()){
            int v=q.front();
            q.pop();
            
            for(auto it:list[v]){
                q.push(it);
                l.push_back(it);
            }
        }
        
        int minimum=INT_MAX;
        for(int i=0;i<quiet.size();i++){
            if(find(l.begin(),l.end(),i)!=l.end())
                minimum=min(minimum,quiet[i]);
        }
        return mp[minimum];
    }
    
    vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet) {
        int n=quiet.size();
        vector<vector<int>> list(n,vector<int>());
        vector<int> ans;
        
        int i;
        for(i=0;i<richer.size();i++)
            list[richer[i][1]].push_back(richer[i][0]);
        for(i=0;i<quiet.size();i++)
            mp[quiet[i]]=i;
        
        for(i=0;i<n;i++){
            int s=bfs(i,list,quiet);
            ans.push_back(s);
        }
        
        return ans;
    */
    }
};