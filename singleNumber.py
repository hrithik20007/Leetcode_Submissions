'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        p=0
        for i in nums:

            #If a number repeats, then the its index() result at the later iterations will not be correct, as that will always give the index of its first occurence. So when such number is found, we don't append it and delete its first occurence as well.
            if nums.index(i)==p:
                a.append(i)
            else:
                a.remove(nums[nums.index(i)])

            p=p+1
        
        return a[0]
