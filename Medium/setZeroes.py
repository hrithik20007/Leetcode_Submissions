'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''





class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        fi=0
        fj=0
        m=len(matrix)
        n=len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0 and i==0:
                    fi=1
                if matrix[i][j]==0 and j==0:
                    fj=1
                if matrix[i][j]==0:         
                    matrix[0][j]=0              #Changing the corresponding matrix element in the first row to 0
                    matrix[i][0]=0              #Changing the corresponding matrix element in the first column to 0
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j]==0 or matrix[i][0]==0:  
                    matrix[i][j]=0                          #Changes the elements in the matrix to 0 if that element's 
                                                            #corresponding first row or first column's element's value is 0
                    
        if fi==1:                                           #Changing the entire first row to 0
            for i in range(n):
                matrix[0][i]=0
                
        if fj==1:                                           #Changing the entire first column to 0
            for i in range(m):
                matrix[i][0]=0
                
                
        
        '''
        This works but I wanted a faster solution
        
        
        
        i1=[]
        j1=[]
        m=len(matrix)
        n=len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    i1.append(i)
                    j1.append(j)
        
        for i in range(m):
            for j in range(n):
                if i in i1 or j in j1:
                    matrix[i][j]=0
        '''
