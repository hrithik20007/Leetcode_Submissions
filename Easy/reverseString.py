'''
Write a function that reverses a string. The input string is given as an array of characters s.
'''



class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        j=0
        for i in s[::-1]:
            s[j]=i
            j+=1
