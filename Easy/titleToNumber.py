'''
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
'''


class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        n=columnTitle
        s=0
        a={}
        j=1
        for i in range(65,91):  #Creating a dictionary with the alphabets as keys and 1-26 as values.
            a[chr(i)]=j  #chr() converts an ASCII to character
            j+=1
        
        for k in n:
            s=s*26+a[k]

        return s
