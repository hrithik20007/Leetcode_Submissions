'''
Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''



class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n1=list(set(nums))    #Logic is that when we make a set out of the items of a list, only the unique charcaters make up the set and the repeating characters are stripped.

        if len(n1)<3:
            n1.sort()
            return n1[-1]  #Returns the last number in the list
        else:
            n1.sort()
            return n1[-3]  #Retruns the third last number in the list
