/*
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed 
edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a 
signal to travel from source to target.
We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is 
impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
*/







/*
Logic:
Solved using Dijkstra's Algorithm. We use a vector 'dis' which will represent the minimum distance of all nodes from
a given node (here, k). Initially, all values are initialised as infinity. If a particular index gives infinity even after
the end of the algorithm (other than the index 0), that means that particular node-index cannot be reached and we return
-1. Essentially we are asked to return the maximum value from all these minimum time paths. It is because, all nodes will
be reached in their minimum times respectively. However, all nodes will have received the signal after the last node 
recieves it (the farthest one, in terms of edge times). 
*/

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        map<int,vector<pair<int,int>>> list;
        vector<bool> vis(n+1,false);
        
        int i;
        for(i=0;i<times.size();i++){
            int u=times[i][0];
            int v=times[i][1];
            int w=times[i][2];
            list[u].push_back({v,w});
        }
        
        const int INF=1e9;
        vector<int> dis(n+1,INF);
        set<pair<int,int>> s;
        dis[k]=0;
        s.insert({0,k});
        
        //For x={wt,vector}
        //For it={vector,weight} (i.e. vectors adjacent to x)
        while(!s.empty()){
            auto x=*(s.begin());
            s.erase(x);
            for(auto it:list[x.second]){
                if(dis[it.first]>dis[x.second]+it.second){
                    s.erase({dis[it.first],it.first});
                    dis[it.first]=dis[x.second]+it.second;
                    s.insert({dis[it.first],it.first});
                }
            }
        }
        
        int maximum=INT_MIN;
        for(i=1;i<=n;i++){
            if(dis[i]==INF)
                return -1;
            maximum=max(maximum,dis[i]);
        }
        
        return maximum;
    
    
    
    
    
    /*
    int dfs(int node, map<int,vector<pair<int,int>>> list, vector<bool> &vis, int s){
        int maximum=INT_MIN;
        vis[node]=true;
        if(list[node].size()==0){
            return s;
        }
        
        for(auto it:list[node]){
            if(vis[it.first]!=true){
                maximum=max(maximum,dfs(it.first,list,vis,s+it.second));
            }
        }
        
        return maximum;
    }
    
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        map<int,vector<pair<int,int>>> list;
        vector<bool> vis(n+1,false);
        
        int i;
        for(i=0;i<times.size();i++){
            int u=times[i][0];
            int v=times[i][1];
            int w=times[i][2];
            list[u].push_back({v,w});
        }
        
        int res=0;
        res=dfs(k,list,vis,0);
        
        int r=0;
        for(i=0;i<=n;i++){
            if(vis[i]==true)
                r+=1;
        }
        
        if(r==n)
            return res;
        else 
            return -1;
    */
    }
};