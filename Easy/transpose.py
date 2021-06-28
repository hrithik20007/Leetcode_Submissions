'''
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
'''






class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        #Compare with example2 for better understanding
        x=[]
        matrix1=[]
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                x.append(matrix[j][i])
            matrix1.append(x)
            x=[]
                
        return matrix1




        #The below two work as well but they are slow

        '''
        matrix1=[[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix1[j][i]=matrix[i][j]
                
        return matrix1
        '''

    #======================================OR==============================================

        '''
        if len(matrix)==len(matrix[0]):
            matrix1=[[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]    
        else:
            matrix1=[[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]    #This case will always work, thus we have lifted the above if statement 
                                                                                        #in the above example.
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix1[j][i]=matrix[i][j]
                
        return matrix1
        '''
