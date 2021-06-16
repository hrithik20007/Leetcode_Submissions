'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and space is marked as 1 and 0 respectively in the grid.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
'''




'''
Logic: Same as uniquePaths plus the added obstacles. The logic is also same as uniquePaths except that when an obstacle is encountered, we change its value to 0
so that the path from that point is not counted.
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    obstacleGrid[i][j]=1
                    continue
                if obstacleGrid[i][j]==1:       #Added portion. Here we change the value of the element to 0.
                    obstacleGrid[i][j]=0
                    continue
                if i>=1:
                    obstacleGrid[i][j]+=obstacleGrid[i-1][j]
                if j>=1:
                    obstacleGrid[i][j]+=obstacleGrid[i][j-1]
        
        return obstacleGrid[m-1][n-1]
        
        
        
        '''
        Time Limit Exceeded 


        def path(self,i,j,m,n,obstacleGrid):
            if i>=m or j>=n:
                return 0
            if obstacleGrid[i][j]==1:          #When an obstacle is encountered, the function is returned with a null value, meaning this path won't be counted
                return 0
            if i==m-1 and j==n-1:
                return 1
            c=self.path(i+1,j,m,n,obstacleGrid)+self.path(i,j+1,m,n,obstacleGrid)
            return c

        def uniquePathsWithObstacles(self, obstacleGrid):
            """
            :type obstacleGrid: List[List[int]]
            :rtype: int
            """
            m=len(obstacleGrid)
            n=len(obstacleGrid[0])
            c1=self.path(0,0,m,n,obstacleGrid)
            return c1
        '''
