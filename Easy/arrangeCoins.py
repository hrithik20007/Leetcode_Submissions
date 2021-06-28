'''
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
'''


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        s=0
        while(s<n):
            s+=i
            i+=1  #Keeps track of the step no.
            
        if s==n:        #This means last step is complete
            return i-1
        elif s>n:       #This condition means the last step is incomplete.
            return i-2
            
