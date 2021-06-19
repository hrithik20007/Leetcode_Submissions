'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
    
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''




class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        n=len(matrix[0])
        
        for i in range(m):
            if target<=matrix[i][n-1]:          #Checks the last element in each row and breaks if target is smaller or equal
                break
        
        for j in range(n):
            if target==matrix[i][j]:            #Strats checking in the row where the first loop breaks
                return True
            
        return False

#=====================BOTH SOLUTIONS WORK=======================        

        
        m=len(matrix)
        n=len(matrix[0])
        i=m-1                                   #Searching starts from bottom left
        j=0 
        while(i<m and i>=0 and j<n and j>=0):
            if target==matrix[i][j]:
                return True
            if(target>matrix[i][j]):            #Goes right if the target is larger
                j+=1
            else:                               #Goes up by default
                i-=1
                
        return False
