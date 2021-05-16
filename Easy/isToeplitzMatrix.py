'''
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:
Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.


[SEE THE PROBLEM IMAGES FOR BETTER UNDERSTANDING]
'''





class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rl=len(matrix)  #No. of rows
        cl=len(matrix[0])   #No. of columns
        
        for i in range(0,rl-1):     #For checking along the first column.
            r=i
            c=0
            while(r<=rl-2 and c<=cl-2):
                if(matrix[r][c]==matrix[r+1][c+1]):
                    r+=1
                    c+=1
                else:
                    return False

        for j in range(0,cl-1):     #For checking along the first row.
            r=0
            c=j
            while(r<=rl-2 and c<=cl-2):
                if(matrix[r][c]==matrix[r+1][c+1]):
                    r+=1
                    c+=1
                else:
                    return False
        
        return True
