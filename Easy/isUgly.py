'''
Given an integer n, return true if n is an ugly number.

Ugly number is a positive number whose prime factors only include 2, 3, and/or 5.
'''



class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:  #1 is typically treated as an ugly number
            return True
        elif n==0:
            return False
        elif n%2!=0 and n%3!=0 and n%5!=0:
            return False
        else:
            while n!=1:
                if n%2==0:
                    n=n//2  #Retruns n as an integer rather than a decimel
                elif n%3==0:
                    n=n//3
                elif n%5==0:
                    n=n//5
                else:
                    n=1
                    return False
            return True
