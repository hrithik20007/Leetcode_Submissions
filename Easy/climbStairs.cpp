/*
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
*/






/*DP Array Solution --> The current array element is the addition of the last two.*/
class Solution {
public:
    int climbStairs(int n) {
        int dp[n];
        dp[0]=1;
        if(n>1)
            dp[1]=2;
        
        for(int i=2;i<n;i++){
            dp[i]=dp[i-1]+dp[i-2];
        }
    
        return dp[n-1];
    }
};





/*
Another Solution using Recursion and Memoization (Same Speed)
*/
class Solution {
public:
    int dp[50];
    int helper(int s, int n){
        if(s==n)
            return 1;
        if(s>n)
            return 0;
        if(dp[s]!=-1)
            return dp[s];
        
        dp[s]=helper(s+1,n)+helper(s+2,n);
        return dp[s];
    }
    
    int climbStairs(int n) {
        memset(dp,-1,sizeof(dp));
        return helper(0,n);
    }
};