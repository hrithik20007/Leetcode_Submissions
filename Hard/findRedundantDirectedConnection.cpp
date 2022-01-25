/*
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other 
nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.
The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), with 
one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge 
that already existed.
The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed 
edge connecting nodes ui and vi, where ui is a parent of child vi.
Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers, 
return the answer that occurs last in the given 2D-array.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
Output: [4,1]
*/







/*
Logic:
We have to make a tree after removing a single edge, and in a tree indegree of a node can either be 1 or 0 .

- Step 1: Calculate the indegree of each node. take a vector of size of n+1(1 based indexing), and store which edge 
contribute to the indegree of that node in the array.
If u find a node whose indree has been already set to an edge means its indegree is 2 i.e that node has two incoming edge 
and we have to remove one of those incoming edge because since only one edge is extra in a tree , therefore there can be 
exactly one node with indegree 2.
- Step 2: If no node has indegree 2 , just apply union find algorithm.
- Step 3: If u find a node with indegree two , store both the edges coming to that node .
- Step 4: Now remove one of the two edges and apply union find , if cycle is not detected then the edge which we removed 
is the edge we actually have to remove , and if cycle detected, then that is not the right edge to remove it is the other 
edge we saved earlier.
*/

class Solution {
public:
    int find_set(int a, vector<int> &parent){           //Gives the parent of the node
        if(a==parent[a])                                                  
            return a;                                                  
        else{
            parent[a]=find_set(parent[a],parent);
            return parent[a];   
        }
    }
    
    vector<int> union_set(vector<int> ans1,vector<int> ans2,vector<int> &parent,vector<int> &size,vector<vector<int>> edges,bool flag){
        
        for(int i=0;i<edges.size();i++){                
            if(edges[i]==ans1)
                continue;
            int a=find_set(edges[i][0],parent);                                          
            int b=find_set(edges[i][1],parent);
            if(a!=b){
                if(a<b){
                    int t=b;
                    b=a;
                    a=t;
                }
                parent[b]=a;
                size[a]+=size[b];
            }
            else{
                if(flag==true)                      //In case of indegree=2, either ans1 or ans2 had to be the answer. (As
                    return ans2;                    //ans2 forms a cycle, that means ans is the required edge)
                return {edges[i][0],edges[i][1]};   //In case of indegree<2, any current edge which forms cycle is the
            }                                       //required answer
        }
        
        return ans1;                                //If no cycle forms without ans1 edge, that means ans1 leads to cycle
    }
    
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        int n=edges.size();
        vector<int> parent(n+1);
        vector<int> size(n+1);
        vector<int> ans1;
        vector<int> ans2;
        vector<int> ind(n+1,-1);
        
        int i;
        for(i=0;i<=n;i++){                                              
            parent[i]=i;                                                //Every node is its parent initially
            size[i]=1;                                                  //with size as 1
        }
        
        for(i=0;i<n;i++){                                               //To check if a node has 2 indegrees
            if(ind[edges[i][1]]!= -1){                                  //Indegree of this node (edges[i][1]) is 2
                ans1 = edges[i];                                        //edge1 which contributes to 2 indegree
                ans2 = edges[ind[edges[i][1]]];                         //edge2 which contributes to 2 indegree
                return union_set(ans1,ans2,parent,size,edges,true);
            }
            
            ind[edges[i][1]] = i;                                       //The edge no. contributing to the indegree of 
        }                                                               //edges[i][1] is i
        

        return union_set(ans1,ans2,parent,size,edges,false);            //Every node has 1 or 0 indegree
    }
};