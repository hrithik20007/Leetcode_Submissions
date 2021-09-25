/*
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are 
allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the 
grid boundary). You can apply at most maxMove moves to the ball.
Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out 
of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
*/






/*
Logic: Using recursion and memoization. Go in all directions and return 1 if the ball goes out the boundary.
If maximum moves is exceeded, we return 0.
*/
class Solution {
public:
    #define ll long long int
    ll dp[52][52][52];
    int mm,nn;
    ll d=1e9+7;
    
    ll helper(int x, int y, int moves){
        if(moves<0)
            return 0;
        if(x>=mm || x<0 || y>=nn || y<0)
            return 1;
        if(dp[x][y][moves]!=-1)
            return dp[x][y][moves];
        
        ll a=0;
        a+=helper(x+1,y,moves-1);a=a%d;
        a+=helper(x,y+1,moves-1);a=a%d;
        a+=helper(x-1,y,moves-1);a=a%d;
        a+=helper(x,y-1,moves-1);a=a%d;
        
        dp[x][y][moves]=(a%d);
        return dp[x][y][moves];
    }
    
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        mm=m;
        nn=n;
        memset(dp,-1,sizeof(dp));
        return helper(startRow, startColumn, maxMove);
    }
};