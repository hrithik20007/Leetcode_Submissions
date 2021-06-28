'''
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0 or x>2**31-1:
            return null
        else:
            y=str(sqrt(x))
            int=y.split(".")[0]
            return int
