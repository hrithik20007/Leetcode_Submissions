'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''





class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rs=0                    #Keeps track of the starting row               
        re=len(matrix)-1        #Keeps track of the ending row
        cs=0                    #Keeps track of the starting column
        ce=len(matrix[0])-1     #Keeps track of the ending column
        l=[]                    #List to show the result
        f=0                     #Keeps track of the continuity of the for loops. Thus, a for loop can't be skipped and if it does, then the loop stops
        
        while(rs<=re and cs<=ce):
            if f==0:
                for i in range(cs,ce+1):
                    l.append(matrix[rs][i])
                rs+=1
                f=1
            
            elif f==1:
                for i in range(rs,re+1):
                    l.append(matrix[i][ce])
                ce-=1
                f=2

            elif f==2:
                for i in range(ce,cs-1,-1):
                    l.append(matrix[re][i])
                re-=1
                f=3

            elif f==3:
                for i in range(re,rs-1,-1):
                    l.append(matrix[i][cs])
                cs+=1   
                f=0

        return l
