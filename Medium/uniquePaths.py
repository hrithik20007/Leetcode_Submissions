'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:
Input: m = 7, n = 3
Output: 28

Example 4:
Input: m = 3, n = 3
Output: 6
'''


'''
Logic: We are adding the numbers such that each grid element will represent the number of ways we can reach it. 
We consider the immideate left horizontal as well as top vertical elements and add them up to get the element in the current box of the grid.
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid=[[0]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    grid[i][j]=1
                    continue
                if i>=1:
                    grid[i][j]+=grid[i-1][j]
                if j>=1:
                    grid[i][j]+=grid[i][j-1]
        
        return grid[m-1][n-1]

        
        
    '''
    This works but the time limit exceeds
    
    
    
    def path(self,i,j,m,n):
        if i>=m or j>=n:
            return 0
        if i==m-1 and j==n-1:
            return 1
        c=self.path(i+1,j,m,n)+self.path(i,j+1,m,n)
        return c
        
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        c1=self.path(0,0,m,n)
        return c1
    '''
