'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''




class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        c=0     #For counting the number of positions where we can place flowers without anyone being adjacent.
        if len(flowerbed)==1:   #For special cases of one-element-list.
            if flowerbed[0]==0:
                flowerbed[0]=1
                c+=1
        
        if flowerbed[0]==0 and flowerbed[1]==0:     #For the starting index
            c+=1
            flowerbed[0]=1

        for i in range(1,len(flowerbed)-1):     #For all the elements between the first and last element
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:     
                flowerbed[i]=1
                c+=1

        if flowerbed[-1]==0 and flowerbed[-2]==0:   #For the ending index
            flowerbed[-1]=1
            c+=1
            
        return c>=n     #If our number of positions is more than the no. given
        '''
        f=1
        if len(flowerbed)==1 and flowerbed[0]==0 and n==1:
            return True
        if flowerbed[0]==0 and flowerbed[1]==0:
            n-=1
        if flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0:
            n-=1        
        for i in range(1,len(flowerbed)):
            if flowerbed[i]==0 and flowerbed[i-1]==0:
                f+=1
            else:
                if f>=3:
                    if f==3:
                        n-=1
                    elif f%2==1:
                        n-=(f-1)//2
                    elif f%2==0:
                        n-=(f-2)//2
                f=1
                
        if n<=0:
            return True
        else:
            return False
        '''      
