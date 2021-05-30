'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
'''




class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1=0
        n2=0
        
        for i in num1:
            n1=n1*10+(ord(i)-48)    #Made them intergers using ASCII values, where integers start from 48.
            
        for i in num2:
            n2=n2*10+(ord(i)-48)
            
        return str(n1*n2)
