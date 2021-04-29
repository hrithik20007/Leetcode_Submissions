'''
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?
'''


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        if n!=0:
            s=1
            c=0
            while(n>0):
                s=n*s
                n-=1
            
            s=str(s)
            n1=int(s[len(s)-1])
            j=2
            while(n1==0):
                c+=1
                n1=int(s[len(s)-j])
                j+=1
            return c
        else:
            return 0
        '''

    
        # I did this because the question asked for logarithmic time complexity even thought the above solution worked. 
        if n==0:
            return 0
        else:

            # // is used for dividing but returns only the integer part.
            # The logic is every power of 5 gives a certain number of zeroes in the factorial. We need the total of that 'certain no. of zeroes'
            return(n//5+ self.trailingZeroes(n//5)) 
