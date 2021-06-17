'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
'''





class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        matrix=[[0]*len(grid[0]) for i in range(len(grid))]
        matrix[0][0]=grid[0][0]
        
        for i in range(1,len(grid[0])):                 #Initialises matrix's first row as cumulative sum
            matrix[0][i]=grid[0][i]+matrix[0][i-1]
            
        for i in range(1,len(grid)):                    #Initialises matrix's first column as cumulative sum
            matrix[i][0]=grid[i][0]+matrix[i-1][0]
    
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                matrix[i][j]=min(grid[i][j]+matrix[i-1][j],grid[i][j]+matrix[i][j-1])   #Each matrix element adds the smaller number from the upper and left box
                                                                                        #to the grid element of the same box
        
        return matrix[len(grid)-1][len(grid[0])-1]
    



    
    '''
    Time Limit Exceeded
    
    
    def path(self,i,j,m,n,s,grid):
        if i>=m or j>=n:
            return 999
        s+=grid[i][j]
        if i==m-1 and j==n-1:
            return s
        c=min(self.path(i+1,j,m,n,s,grid),self.path(i,j+1,m,n,s,grid))
        return c
    
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        c1=self.path(0,0,m,n,0,grid)
        return c1
    '''
