'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
'''





#Logic: Take a look at 'spiralOrder.py' for main explaination.
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rs=0
        re=n-1
        cs=0
        ce=n-1
        f=0
        j=1
        
        matrix=[[0]*n for i in range(n)]            #Initializes matrix with its elements as 0
        
        while(rs<=re and cs<=ce):
            if j<=n**2:
                if f==0:
                    for i in range(cs,ce+1):
                        matrix[rs][i]=j
                        j+=1
                    rs+=1
                    f=1

                elif f==1:
                    for i in range(rs,re+1):
                        matrix[i][ce]=j
                        j+=1
                    ce-=1
                    f=2

                elif f==2:
                    for i in range(ce,cs-1,-1):
                        matrix[re][i]=j
                        j+=1
                    re-=1
                    f=3

                elif f==3:
                    for i in range(re,rs-1,-1):
                        matrix[i][cs]=j
                        j+=1
                    cs+=1   
                    f=0

        return matrix
