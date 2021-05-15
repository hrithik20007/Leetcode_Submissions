class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        l=[2,3,5,7,11,13,17,19,23,29,31]  #We can only do this in case of bits because upper limit is 32 for signed integers
        c=0
        for i in range(left,right+1):
            a=bin(i)[2:]
            n=a.count("1")
            if n in l:
                c+=1
                
        return c
        '''
        This is my solution and it works but I wanted a faster solution
        
        
        f=0
        c=0
        for i in range(left,right+1):
            a=bin(i)[2:]
            n=a.count("1")
            if n==1 or n==0:
                f+=1
            for j in range(2,n):
                if n%j==0:
                    f+=1
            if f==0:
                c+=1
            else:
                f=0
                
        return c
        '''
