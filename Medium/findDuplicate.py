'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [1,1]
Output: 1

Example 4:
Input: nums = [1,1,2]
Output: 1
'''





'''
Logic: We think of this list as a linked list. Each element points to its value's index. So in first example, 1 points to index1 or 3. 3 points to 2. 4 points to 2.
Both 2s will point to 4 at index 2. Thus we will find that we have a cyclic linked list, with the cycle starting at 2. We use the 'tortoise and hare' method to find
a point within the cycle. From that point, we start slow and we start slow2 from the beginning of the linked list. The point they will converge at will be the
starting point of the cycle or the repeated element. That is, 2 here.
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=0,0
        while True:
            slow=nums[slow]                 #Moves by 1 step
            fast=nums[nums[fast]]           #Moves by 2 steps
            if slow==fast:
                break

        slow2=0
        while True:
            slow=nums[slow]                #Both move by 1 step
            slow2=nums[slow2]
            if slow==slow2:
                return slow
