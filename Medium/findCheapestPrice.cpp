/*
There are n cities connected by some number of flights. You are given an array flights where 
flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If 
there is no such route, return -1.

Example 1:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
*/







/*
Logic:
Solved using Bellman-Ford algorithm to find the shortest path from source to destination within (k+1) steps, however with 
a little modification. k+1 because we know for n vertices, Bellman Ford uses n-1 iterations for n-1 vertices (other than 
the source). k is the number excluding source and destination. So k+1 is the number only exclusing the source. 
Now, Bellman Ford gives proper distances only after a certain number of iterations (n-1 or less). If we stop the iteration
at k+1, then the distance of destination may not be correct. What we do is that we use a temporary vector 'temp' to store
those distances only which will give us the correct distance (at each iteration). Then we update our original distance
vector after every iteration with the temp.

Why do we get incorrect values at a stage and how the process fixes it--
Take the second example. After first iteration, if we didn't use temp vector, the dis to 1 would have been 100 while to
2, it would have been 200. However, at first iteration, we can only use one path (for the source), i.e. the 100 path to 1 
and the 500 path to 2. So we temporarily do not consider the changes made to dis[1] (which is 100), so as to get our 
initial dis[1] as infinity. So obviously we will get dis[2] as 500 (since 0+500=500<infinity), instead of 
(100(of dis[1]) +100=200<infinity). In conclusion, we can only correctly change the dis values to source at first 
iteration.
*/

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<int> dis(n,INT_MAX); 
        dis[src]=0;
        vector<int> temp=dis;
        
        for(int i=0;i<=k;i++){
            for(auto it:flights){
                int u=it[0];
                int v=it[1];
                int w=it[2];
                if(dis[u]!=INT_MAX && dis[u]+w<temp[v]) 
                    temp[v]=dis[u]+w;
            }
            dis=temp;
        }
        
        if(dis[dst]==INT_MAX) return -1;
        return dis[dst];
        
    /*
    Gives TLE
    
    
    vector<vector<pair<int,int>>> ans;
    void bfs(int src,int dst,map<int,vector<pair<int,int>>> graph){
        queue<vector<pair<int,int>>> q;
        vector<pair<int,int>> l;
        l.push_back({src,0});
        q.push(l);
        
        while(!q.empty()){
            vector<pair<int,int>> l1=q.front();
            q.pop();
            pair<int,int> back=l1.back();
            if(back.first==dst)
                ans.push_back(l1);
            for(auto it:graph[back.first]){
                l1.push_back({it.first,it.second});
                q.push(l1);
                l1.pop_back();
            }
        }
        
        return;
    }
    
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        map<int,vector<pair<int,int>>> graph;
        
        int i,j;
        for(i=0;i<flights.size();i++){
            int u=flights[i][0];
            int v=flights[i][1];
            int c=flights[i][2];
            graph[u].push_back({v,c});
        }
        
        bfs(src,dst,graph);
        
        int cost;
        int minimum=INT_MAX;
        if(ans.size()==0)
            return -1;
        for(i=0;i<ans.size();i++){
            if(ans[i].size()-2>k)
                continue;
            else{
                cost=0;
                for(j=0;j<ans[i].size();j++)
                    cost+=ans[i][j].second;
                minimum=min(minimum,cost);
            }
        }
        
        if(minimum==INT_MAX) return -1;
        return minimum;
    */
    }
};