'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''





# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        h= n
        l= 1
        if isBadVersion(1)==True:
            return 1      
        elif isBadVersion(n-1)==False:
            return n
        else:
            while(h>l):
                mid=(l+h)//2
                if isBadVersion(mid)==True:
                    h=mid
                else:
                    l=mid+1
                
            return h
        
        '''
        Memory Error
        
        
        else:
            for i in range(1,n+1):
                if isBadVersion(i)==True:
                    return i
                    break
        '''     
