/*
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
*/






/*
Logic: We traverse the 2D vector and make a vector containing the different diagonal elements in different vectors. We wll notice that the no. of diagonals for a 
M*N matrix will be M+N-1. After traversal and making the vector of vectors, we can individually go over those vectors and push the elements into an answer vector.
However, we have to note that the diagonal vectors at even indexes should be pushed in the reverse order.
*/
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        vector<vector<int>> l(mat.size()+mat[0].size()-1);
        vector<int> ans;
        
        int i,j;
        for(i=0;i<mat.size();i++){
            for(j=0;j<mat[0].size();j++){
                l[i+j].push_back(mat[i][j]);
            }
        }
        
        for(i=0;i<l.size();i++){
            if(i%2!=0){
                for(j=0;j<l[i].size();j++)
                    ans.push_back(l[i][j]);    
            }
            else{
                for(j=l[i].size()-1;j>=0;j--)
                    ans.push_back(l[i][j]);
            }
        }
        
        return ans;
    }
};
