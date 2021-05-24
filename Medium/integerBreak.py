'''
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
Return the maximum product you can get.

Example 1:
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.


Both the solutions work and have the same speed more or less.
'''





class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
            return 1
        elif n==3:
            return 2

        '''
        We are dividing the number into 3s and 2s. Every number is made up groups of 2s and 3s.  It is better to count as many of them as 
        possible as 3,3(i.e. 3*3=9) is better than 6.
        '''
        n3=n//3
        n2=0
        
        if n%3==1:      
            n3-=1
            n2=2
        elif n%3==2:
            n2=1
        return (2**n2)*(3**n3)  #Say we found 3 2s, then we do 2*2*2 or 2**3. Same for number of 3s.



        #===================OR====================

        
        l=[]        #This list is to store all possible products
        if n==2:
            return 1
        elif n==3:
            return 2
        else:
            for i in range(2,(n//2)+1):     #i denotes the integers we divide the number n with (we are taking till half of n because after that we
                                            #can only divide them into 2s which certainly wont give us the maximum product.

                n2=1
                if n%i==0:
                    n1=n//i
                    l.append(n1**i)         #Example: 9//3=3. i.e. 3+3+3=9. So we append (3**3=27)
                    
                else:
                    r=n%i                   #Example: For 11//3=3 and r=2. So we make an array of 3 3s in l1 and add 1 to 2(i.e. r) elements in l1.
                                            #So ultimately the numbers become 3,(3+1),(3+1) or 3,4,4
                    n1=n//i
                    l1=[n1]*i
                    for i in range(r):
                        l1[i]+=1
                    for j in range(len(l1)):    #Taking 11's example again, we do 3*4*4=48 and we append 48 into l
                        n2*=l1[j]
                    l.append(n2)

        return max(l)   #We return the maximum product we found
