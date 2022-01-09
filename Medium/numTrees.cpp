/*
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of 
unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1
*/








/*
Logic: 
Solved using the catalan number series logic, which means for n number of nodes, no. of possible BSTs will be given by 
the catalan number for that number 'n'.
Catalan Number for 'n'=CoCn-1+C1Cn-2.....+Cn-1Co, where C is the binomial coefficient. 
We have solved using dynamic programming and memoization. Base cases are -
For n=0 or n=1, answer is 1. 
For n=2, answer is 2.
*/

class Solution {
public:
    long long dp[20];
    
    int catalan(int n){
        if(n==1 || n==0)
            return 1;
        if(n==2)
            return 2;
        if(dp[n]!=0)
            return dp[n];
        
        long long s=0;
        for(int i=0;i<n;i++){
            s+=catalan(i)*catalan(n-i-1);
        }
        
        dp[n]=s;
        return dp[n];
    }
    
    int numTrees(int n) {
        memset(dp,0,sizeof(dp));
        return catalan(n);
    }
};