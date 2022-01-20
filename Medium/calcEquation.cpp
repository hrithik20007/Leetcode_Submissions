/*
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and 
values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for 
Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that 
there is no contradiction.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
*/








/*
Logic:
a/b is joined as a->b (weight of edge becomes the value) as well as b->a (weight of edge becomes the reciprocal value) in 
a graph. Suppose we have a/b and b/c, and we need to find a/c, thus the graph will be a->b->c and we just multiply the
weight of the edges while going from a to c. 
Note: In the problem, strings like "ac" are treated as separate string entirely and not "a*c".
To make the adjacency list, we use a map with the string alphabets as the keys. The values are vectors of pairs with the
first element as the neighbour alphabet and the second element as the weight of the edge joining them. If the alphabets
are present in the graph, then only we can find their division. If either is absent, we return -1.0. To solve for the 
division, we use DFS, treating the numerator as the source while the denominator as the destination. If such a path exists,
we return the multiplication of the edge weights, otherwise -1.0.
*/

class Solution {
public:
    double dfs(string s,string d,map<string, vector<pair<string,double>>> list,map<string,bool> &vis, double res){
        if(s==d)
            return res;
        
        vis[s]=true;
        
        double ans=-1.0;
        for(auto it:list[s]){
            double ans=-1.0;
            if(vis[it.first]!=true){
                res*=it.second;   
                ans=dfs(it.first,d,list,vis,res);
                res/=it.second;
            }
            if(ans!=-1.0)
                return ans;
        }
        
        if(ans==-1.0) return -1.0;
        else return ans;
    }
    
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        map<string, vector<pair<string,double>>> list;
        map<string,bool> present;
        vector<double> ans;
        
        int i;
        for(i=0;i<equations.size();i++){
            string u=equations[i][0];
            string v=equations[i][1];
            double d=values[i];
            list[u].push_back({v,d});
            list[v].push_back({u,1/d});
            present[u]=true;
            present[v]=true;
        }
        
        for(i=0;i<queries.size();i++){
            double res=-1.0;
            map<string,bool> vis;
            string s=queries[i][0];
            string d=queries[i][1];
            
            if(present[s] && present[d])
                res=dfs(s,d,list,vis,1.0);
            ans.push_back(res);
        }
        
        return ans;
    }
};