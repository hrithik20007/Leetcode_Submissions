'''
Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number
Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
You may assume that each input would have exactly one solution and you may not use the same element twice.
'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(numbers)-1
        while(i<j):
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            
            #As the list is already sorted in ascending order, thus the target being smaller than the sum would indicate that the second value has passed the necessary(i.e. its much larger)
            elif numbers[i]+numbers[j]>target:
                j-=1
            else:
                i+=1
        '''
        As time limit exceeded
        
        for i in range(0,len(numbers)-1):
            for j in range(i+1,len(numbers)):
                s= numbers[i]+numbers[j]
                if s==target:
                    p=i
                    q=j
                    break
        
        return [p+1,q+1]
        '''
