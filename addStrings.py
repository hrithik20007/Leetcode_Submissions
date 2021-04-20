'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
'''



class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1=int(num1)
        n2=int(num2)
        return str(n1+n2)
