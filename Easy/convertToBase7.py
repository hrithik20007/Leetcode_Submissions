'''
Given an integer num, return a string of its base 7 representation.

Example 1:
Input: num = 100
Output: "202"

Example 2:
Input: num = -7
Output: "-10"
'''




class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        else:
            n=abs(num)
            s=[]
            while(n>0):
                n1=n%7
                s.append(str(n1))
                n=n//7
        s=''.join(reversed(s))
        if num>0:
            return s
        else:
            return ("-"+s)
        '''
        i=0
        while(7**i<=abs(num)):
            i+=1
        if 7**(i-1)==abs(num):
            s=[0]*(i-1)+[1]
        else:
            s=[0]*i
            n1=num%7
            s[0]=n1
            a2=sys.maxsize
            n2=num//7
            n3=n2*7
            j=1
            while(a2!=0):
                a1=n3//(7**(len(s)-j)
                s[len(s)-j]=a1
                a2=n3%(7**(len(s)-j)
                n3=a2
                j-=1
            
            s= "".join(reversed(s))
            if num>0:
                return s
            else:
                return ("-"+s)
        '''
