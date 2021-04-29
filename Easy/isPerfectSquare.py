'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
'''



class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        '''
        This is my solution but I wanted a faster solution
        
        
        if num==0:
            return False
        elif num==1:
            return True
        else:
            x=2
            f=0
            while (x**2<=num):
                if x**2==num:
                    f+=1
                    break
                x+=1
                
            if f==0:
                return False
            else:
                return True
        '''
        return (num**0.5)%1==0
