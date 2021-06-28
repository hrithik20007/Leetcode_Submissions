#Reverse an integer such that the result remains within the 32-bit interger range.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #Extended slice or [start:stop:step] helps to arrange or iterate over a string. By default, start becomes 0 and stop becomes the string length
        s=int(str(abs(x))[::-1])
        if s >= 2**31-1 or s <= -2**31:
            return 0
        else:
            if(x<0):
                return -1*s
            else:
                return s
