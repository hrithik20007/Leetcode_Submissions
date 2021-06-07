'''
You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).
After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.
Return the total surface area of the resulting shapes.
Note: The bottom face of each shape counts toward its surface area.

Example 1:
Input: grid = [[2]]
Output: 10

Example 2:
Input: grid = [[1,2],[3,4]]
Output: 34

Example 3:
Input: grid = [[1,0],[0,2]]
Output: 16

Example 4:
Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 32

Example 5:
Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
Output: 46

LOOK AT THE DIAGRAMS IN THE QUESTION
'''





class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n=len(grid)
        r=0
        for i in range(n):
            for j in range(n):
                if grid[i][j]>0:                            #Top and bottom surfaces
                    r+=2
                    
                if i==0:                                    #These four are the outer surface areas
                    r+=grid[i][j]
                if i==n-1:
                    r+=grid[i][j]
                if j==0:
                    r+=grid[i][j]
                if j==n-1:
                    r+=grid[i][j]
                
                if i!=0:                                    #These four check the adjacent four cubes for height difference which will lead to surface area
                                                            #towards the inside
                    if grid[i][j]>grid[i-1][j]:
                        r+=(grid[i][j]-grid[i-1][j])
                if i!=n-1:
                    if grid[i][j]>grid[i+1][j]:
                        r+=(grid[i][j]-grid[i+1][j])
                if j!=0:
                    if grid[i][j]>grid[i][j-1]:
                        r+=(grid[i][j]-grid[i][j-1])
                if j!=n-1:
                    if grid[i][j]>grid[i][j+1]:
                        r+=(grid[i][j]-grid[i][j+1])
                        
        return r


        #=======================================OR=============================================
        '''
        n=len(grid)
        r=0
        for i in range(n):
            for j in range(n):
                if grid[i][j]>0:
                    r+=2
                    
                if i==0:
                    r+=grid[i][j]
                if i==n-1:
                    r+=grid[i][j]
                if j==0:
                    r+=grid[i][j]
                if j==n-1:
                    r+=grid[i][j]
                
                if i!=n-1:
                    r+=abs(grid[i][j]-grid[i+1][j])
                if j!=n-1:
                    r+=abs(grid[i][j]-grid[i][j+1])
                        
        return r
        '''
