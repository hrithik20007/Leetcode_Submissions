#Returns true if palindrome otherwise false

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        r=str(x)[::-1]
        return (bool(r==str(x)))
