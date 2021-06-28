'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
'''


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=[]
        if n==1 or n==7:
            return True
        else:
            while(n!=1):
                tsum = sum([int(i)**2 for i in str(n)]) #sum() in python adds the elements of a list which we provide as an arguement

                if tsum in s: #If tsum repeats, that means the addition froms a loop and will never add up to 1
                    return False
                else:
                    s.append(tsum)
                n=tsum 
                
        return True
        '''
        s=0
        n1=str(n)
        while(int(n1)>9):
            for i in n1:
                s=s+int(i)**2
            n1=s
            n1=str(n1)

        if n==1 or n==7:
            return True
        if n1==1:
            return True
        else:
            return False
        '''



        '''
        if n==1 or n==7:
            return True 
        else:
            s=0
            a=n
            f=0
            while(a>9):
                while(n>0):
                    d=int(n%10)
                    s=int(s+d**2)
                    n=int(n/10)
                if s==1:
                    f+=1
                    break
                else:
                    n=s
                s=0
                a=n

            if f==0:
                return False
            else:
                return True
        '''
