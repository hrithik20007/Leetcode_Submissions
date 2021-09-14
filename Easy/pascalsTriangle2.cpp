/*
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
*/





/*
Logic: Same as Pascal's Triangle problem. Only difference is here we return the last row only (instead of the
whole vector). That is the rowIndex-th row (even though it is 0-indexed).
*/
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> ans(rowIndex+1);
        int i,j;
        
        for(i=0;i<=rowIndex;i++){
            ans[i].resize(i+1);
            ans[i][0]=ans[i][i]=1;
            for(j=1;j<i;j++)
                ans[i][j]=ans[i-1][j-1]+ans[i-1][j];
        }
        
        return ans[rowIndex];
    }
};