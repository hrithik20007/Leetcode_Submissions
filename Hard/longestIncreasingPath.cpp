/*
Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move 
outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1
*/







/*
Logic:
Using DFS and memoization. We travel to the four directions (only if they exist and if the elements in those directions
are greater) and recursively call the function again there. We use a vector 'vis' which keeps track of matrix nodes visited
and the longest path starting from that node (like a cache). Finally, we use 'maximum' variable to keep track of the 
maximum value from the 'vis' 2D vector.
*/

class Solution {
public:
    int helper(int i,int j,int m,int n,vector<vector<int>>& matrix,vector<vector<int>> &vis, int &maximum){
        if(vis[i][j]!=-1)
            return vis[i][j];
        
        int a=1,b=1,c=1,d=1;
        if(i!=0 && matrix[i-1][j]>matrix[i][j])
            a=helper(i-1,j,m,n,matrix,vis,maximum)+1;
            
        if(j!=0 && matrix[i][j-1]>matrix[i][j])
            b=helper(i,j-1,m,n,matrix,vis,maximum)+1;
        
        if(i!=m-1 && matrix[i+1][j]>matrix[i][j])
            c=helper(i+1,j,m,n,matrix,vis,maximum)+1;    
        
        if(j!=n-1 && matrix[i][j+1]>matrix[i][j])
            d=helper(i,j+1,m,n,matrix,vis,maximum)+1;    
        
        vis[i][j]=max(a,max(b,max(c,d)));
        return vis[i][j];
    }
    
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int m=matrix.size();
        int n=matrix[0].size();
        vector<vector<int>> vis(m,vector<int>(n,-1));
        
        int i,j,maximum=INT_MIN;
        for(i=0;i<m;i++){
            for(j=0;j<n;j++){
                if(vis[i][j]==-1)
                    maximum=max(maximum,helper(i,j,m,n,matrix,vis,maximum));
                else
                    maximum=max(maximum,vis[i][j]);
            }
        }
        
        return maximum;
    }
};