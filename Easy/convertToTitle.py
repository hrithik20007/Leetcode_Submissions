'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 2:
Input: columnNumber = 701
Output: "ZY"

Example 3:
Input: columnNumber = 2147483647
Output: "FXSHRXW"
'''



class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s2=""
        n=columnNumber
        while n>0:
            s2=s1[int(n-1)%26]+s2
            n=int(n-1)/26
            
        return s2
        '''
        a={}
        s=""
        b=65
        for i in range(1,27):
            a[i]=chr(b)  #chr() changes ASCII to characters while ord() does the opposite
            b+=1
            
        d=columnNumber/26
        r=columnNumber%26
            
        for i in range(0,d):
            s=s+"A"
            
        s=s+str(a[r])
        
        return s
        '''
