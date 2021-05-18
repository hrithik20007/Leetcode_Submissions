'''
x is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.
A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
Now given a positive number n, how many numbers x from 1 to n are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
'''

#Note: 0,1 or 8 cannot form good nos. on their own. However, when joined with 2,5,6 or 9, they can.



class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        for i in range(1,n+1):
            if '3' in str(i) or '4' in str(i) or '7' in str(i):
                continue
            if '2' in str(i) or '5' in str(i) or '6' in str(i) or '9' in str(i):
                c+=1
        
        return c
        '''
        This works but I wanted a faster solution
        
        
        c=0
        f=0
        l=[i for i in range(1,n+1)]
        for j in l:
            n1=j
            if j<10:
                if j==2 or j==5 or j==6 or j==9:
                    c+=1
            else:
                c1=Counter(list(str(j)))    #Checking if the number contains only 0, 1 or 8
                for i in c1:
                    if i=='0' or i=='1' or i=='8':
                        f+=c1[i]

                if f==len(str(j)):
                    f=0
                    continue    #If yes, then we skip it
                f=0
                
                while(j>0):     #If no, we proceed
                    d=int(j%10)
                    if d==2 or d==5 or d==6 or d==9 or d==0 or d==1 or d==8:
                        f+=1
                    j=j//10
                    
                if f==len(str(n1)):
                    c+=1
                f=0
                
        return c
        '''
