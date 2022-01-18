/*
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one 
center node and exactly n - 1 edges that connect the center node with every other node.
You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes 
ui and vi. Return the center of the given star graph.

Example 1:
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

Example 2:
Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1
*/






/*
Logic:
If all edges point to a particular node, that means either the first node or second mode from the the first edge (or any
other edge for that matter) should be present at one end of all the edges (We only consider the second edge here).
*/
class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        int a=edges[0][0];
        int b=edges[0][1];
        if(a==edges[1][0] || a==edges[1][1])
            return a;
        else
            return b;
        
        return -1;
        

        /*
        This also works but slower


        map<int,int> mp;
        int n=edges.size()+1;
        for(int i=0;i<n-1;i++){
            mp[edges[i][0]]+=1;
            mp[edges[i][1]]+=1;
        }
        
        //If the graph didn't have exactly n-1 edges(i.e. one less than edges list size), we would have needed to find n 
        //like this---
        //int n=0;
        //for(auto it:mp){
            //if(it.second>=1)
                //n+=1;
        //}
        
        
        for(auto i:mp){
            if(i.second==n-1)
                return i.first;
        }
        
        return -1;
        */
    }
};