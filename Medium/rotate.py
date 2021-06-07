'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:
Input: matrix = [[1]]
Output: [[1]]

Example 4:
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]


LOOK AT THE DIAGRAMS IN THE QUESTION
'''






class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):                                    #Step1: Transpose
            for j in range(i,len(matrix[0])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                
        for i in range(len(matrix)):                                    #Step2: Horizontal Mirroring
            for j in range(len(matrix[0])//2):
                matrix[i][j],matrix[i][len(matrix[0])-1-j]=matrix[i][len(matrix[0])-1-j],matrix[i][j]
                
        '''
        This works as well but I wanted a faster solution
        
        
        m1=deepcopy(matrix)         #deepcopy() makes a copy without any reference to the original 
        n=len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[j][(n-1)-i]=m1[i][j]
        '''
