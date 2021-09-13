/*
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
*/






/*
Logic: Every j-th column is the sum of j-th and (j-1)-th column's elements of the previous row, except the first 
and last element which is 1.
*/
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans(numRows);
        int i,j;
        
        for(i=0;i<numRows;i++){
            ans[i].resize(i+1);                         //Resizes the vector and initialises its elements with 0
                                                        //(unless the element is explicitly mentioned)
            ans[i][0]=ans[i][i]=1;
            for(j=1;j<i;j++)
                ans[i][j]=ans[i-1][j-1]+ans[i-1][j];
        }
        
        return ans;
    }
};