'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
'''

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        f=0
        x1=bin(x)[2:]      #bin() converts the the no. to the string form of its binary value.
        y1=bin(y)[2:]
        
        if x>y:     #Converting the smaller number to x1 (if the smaller no. is already x1, it is not affected).
            t=x1
            x1=y1
            y1=t
            
        x2=x1.zfill(len(y1))    #zfill() fills the left side of the string with 0s so that its resultant string length becomes equal to the one in the parameter.
        
        for i in range(len(x2)):
            if x2[i]!=y1[i]:
                f+=1
                
        return f

        
