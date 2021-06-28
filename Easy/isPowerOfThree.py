'''
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
'''



class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x=0
        f=0
        while(3**x<=n):
            if 3**x==n:
                f+=1
            x+=1
            
        if f!=0:
            return True
        else:
            return False
