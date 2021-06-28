'''
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
'''



class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l1=[]
        l2=[]
        f=0
        for i in range(left,right+1):
            l1.append(i)
        for j in l1:
            j1=str(j)   #Converting each number in the range to a string, so that we an easily iterate over their characters.
            if len(j1)>1:
                for k in j1:
                    if int(k)==0 or j%int(k)!=0:    #First case is for cases like 10, where diving 10 by 0 will give us a runtime error.
                        f+=1
                        break
            if f==0:
                l2.append(j)
            f=0
            
        return l2
