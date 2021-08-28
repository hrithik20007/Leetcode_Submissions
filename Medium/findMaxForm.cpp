/*
You are given an array of binary strings strs and two integers m and n.
Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
A set x is a subset of a set y if all elements of x are also elements of y.

Example 1:
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
*/






/*
Logic: We use the dp array for memoization instead of a map.
*/
class Solution {
public:
    int dp[102][102][602];
    int helper(vector<string>& strs, int idx, int m, int n){
        if(dp[m][n][idx]!=-1)
            return dp[m][n][idx];
        if(idx>=strs.size())
            return 0;
        
        int m1=0,n1=0,i,a=0,b=0,c=0;
        for(i=0;i<strs[idx].length();i++){
            if(strs[idx][i]=='0')
                m1+=1;
            else
                n1+=1;
        }

        if(m-m1>=0 && n-n1>=0){
            a=1+helper(strs,idx+1,m-m1,n-n1);						//Here, we add string[idx] for next recursive call (1 is added to signify that the list size has 
            														//increased by 1)
            b=helper(strs,idx+1,m,n);								//Here, we do not add string[idx]
        }
        else
            c=helper(strs, idx+1, m, n);							//We have not added string[idx], as it will exceed the number of 0s and 1s allowed
        
        return dp[m][n][idx]=max(a,(max(b,c)));						//max of a,b and c is declared as dp[m][n][idx]'s element
    }
    
    int findMaxForm(vector<string>& strs, int m, int n) {
        memset(dp,-1,sizeof(dp));									//By memset, all the elements of the dp array have been initialised to -1.
        return helper(strs, 0, m, n);
    }
};
