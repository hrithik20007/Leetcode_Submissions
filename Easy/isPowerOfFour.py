'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
'''



class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x=0
        f=0
        while(4**x<=n):
            if 4**x==n:
                f+=1
            x+=1
            
        if f!=0:
            return True
        else:
            return False
