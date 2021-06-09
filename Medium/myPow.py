'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
'''




class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n>0:
            p=n
        else:
            p=-n
        ans=1
        while(p>0):
            if p%2==1:
                ans=ans*x
                p-=1
            else:
                x=x*x               #Taking example of n=6, then at first x becomes x^2 and then ans=x^2 , then x=x^4 and then ans=x^2*x^4. Thus ans becomes x^6.
                p=p//2
                
        return ans if n>0 else 1/ans
        
        
        
        
        '''
        Time Limit Exceeded
        
        
        if n==0:
            return 1
        if n==1:
            return x
        p=1
        n3=abs(n)
        if n3>10:
            n1=n3//10
            n2=n3-(n1*10)
            for i in range(n1):
                p=p*x*x*x*x*x*x*x*x*x*x

            for i in range(n2):
                p=p*x
            
            if n<0:
                return 1/p
            else:
                return p
            
        else:
            for i in range(n3):
                p=p*x

            if n<0:
                return 1/p
            else:
                return p
        '''
