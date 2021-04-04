'''
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        f=0
        x=0
        while(2**x<=n):
            if 2**x==n:
                f=1
            x+=1
        
        if f==1:
            return True
        else:
            return False
