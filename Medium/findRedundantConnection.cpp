/*
In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added 
edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as 
an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return 
the answer that occurs last in the input.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
*/






/*
Logic:
Solved using Disjoint Set Union (DSU) logic. If both nodes have same parents, that means a cycle is found. 
*/

class Solution {
public:
    bool cycle=false;
    
    int find_set(int a, vector<int> &parent, vector<int> &size){            //Gives the parent of a particular node
        if(a==parent[a])                                                    //Also, makes all the nodes in the set have 
            return a;                                                       //the same parent.
        else{
            parent[a]=find_set(parent[a],parent,size);
            return parent[a];   
        }
    }
    
    void union_set(int a,int b, vector<int> &parent, vector<int> &size){    //The parent of the set with higher size 
                                                                            //becomes the parent of the set with lesser
        a=find_set(a,parent,size);                                          //size. The sets are joined.
        b=find_set(b,parent,size);
        if(a!=b){
            if(a<b){
                int t=b;
                b=a;
                a=t;
            }
            parent[b]=a;
            size[a]+=size[b];
        }
        else
            cycle=true;
        
        return;
    }
    
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        const int n=1e5+6;
        vector<int> parent(n);
        vector<int> size(n);
        
        int i,u,v;
        for(i=0;i<edges.size();i++){
            u=edges[i][0];
            v=edges[i][1];
            parent[i]=i;                                            //Initially, every node is its own parent
            size[i]=1;                                              //Initially, the size of every node is 1.
        }
        
        vector<int> v1;
        for(i=0;i<edges.size();i++){
            u=edges[i][0];
            v=edges[i][1];
            union_set(u,v,parent,size);
            if(cycle==true)                                         //
                v1=edges[i];                                        //This portion is done so that v1 stores the last
            cycle=false;                                            //vector which contributes to a cycle.
        }
        
        return v1;
    }
};