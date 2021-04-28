'''
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.

Example 1:
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
'''



class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return False
        else:
            n=int(round(sqrt(num)))
            l=[1]
            for i in range(2,n+1):
                if num%i==0:
                    l.append(i)
                    n2=num//i
                    l.append(n2)
    
            if num==sum(l):
                return True
            else:
                return False
