/*
Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is the product of some 
integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
*/






/*
Logic: Solved using DP. We already define the minimum sqaures required for 0,1 and 2 -
0-> Nothing (0)
1->1 (1)
2->1+1 (2)

Now, we start a loop from 3 until n. At each position, we go back by square indexes (1,4,9.. until [i-the square]
stays >=0 as we do not have dp[-1],dp[-2] etc.) to see the minimum squares making up that index value. We add 1
to the value and check for the minimum values of all such combinations.

For example, let's take 4.
dp array initially -> dp[0,1,2,undefined,undefined]

We start from i=3.
From i, we can go back by value -
-- 1, i.e. dp[2], which is 2. We then add 1, giving us 3.
-- 4, i.e. dp[-1], which is invalid and here we break. 
Minimum value we get is 3, meaning 3 --> dp[2]+1 or (1+1)+1 (minimum no. of squares = 3). So, dp[3]=3.

From i=4, we can go back by value -
-- 1, i.e. dp[3], which is 3. We then add 1, giving us 4. [Meaning (1+1+1)+1]
-- 4, i.e. dp[0], which is 0. We then add 1, giving us 1. 
Minimum value we get from (4 and 1) is 1, meaning 4 --> dp[0]+1 or (0)+1 (minimum no. of squares = 1). 
So, dp[4]=1. This makes sense as 4 itself is a perfect square and only needs 4 itself.

Finally, we return dp[n], which is dp[4]=1.
*/
class Solution {
public:
    int numSquares(int n) {
        if(n==1)
            return 1;
        
        vector<int> dp(n+1);
        dp[0]=0;
        dp[1]=1;
        dp[2]=2;
        
        int i;
        for(i=3;i<=n;i++){
            int j=1,ans=INT_MAX;
            while(i-(j*j)>=0){
                ans=min(ans,1+dp[i-(j*j)]);
                j+=1;
            }
            
            dp[i]=ans;
        }
        
        return dp[n];
    }
    
    
    /*
    int dp[10002][102];
    
    int helper(int idx,int r,int n,int c){
        if(n==0)
            return c;
        if(n<0 || idx>r)
            return INT_MAX;
        if(dp[n][idx]!=-1)
            return dp[n][idx];
        
        int i,a=1;
        for(i=idx;i<=r;i++){
            dp[n][idx]=min(helper(idx,r,n-(i*i),c+1),helper(idx+1,r,n,c));
        }
        
        return dp[n][idx];
    }
    
    int numSquares(int n) {
        int r=sqrt(n);
        memset(dp,-1,sizeof(dp));
        
        return helper(0,r,n,0);
    }
    */
};