#Count the number of prime numbers less than a non-negative number, n.


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        n1=n*[True]  #Gives a list of n 'True' values
        c=0
        
        for i in range(2,n):  #Works on the logic that all the squared numbers including 4 and their increaments of the number are not prime (Eg: n=10, for 2-> 4,6,8 ; for 3->9 ; they won't be prime)
            if n1[i]:
                c+=1
            for j in range(i**2,n,i):
                n1[j]=False
                
        return c
    
        '''
        Time limit exceeded
        
        f=0
        if n<0 or n>5*10**6:
            return None
        elif n==0 or n==1 or n==2:
            return 0
        else:
            j=2
            while(j<n):
                c=0
                for i in range(1,int(j/2)+1):
                    if(j%i==0):
                        c+=1
                if c==1:
                    f+=1
                j+=1
            
        return f
        '''
