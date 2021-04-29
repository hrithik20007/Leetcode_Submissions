'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
'''



class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        n1=0
        n2=1
        if n==1 or n==0:
            return n
        else:
            j=1
            while(j<n):
                s=n1+n2
                n1=n2
                n2=s
                j+=1
            return s
