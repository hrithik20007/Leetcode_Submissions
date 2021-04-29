#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        p=0
        #Capture the position of the target in the list
        for i in nums:
            if i==target:
                p=nums.index(i)
        
        #If the target is not present in the list, we first store it there such that the list is sorted. Then we find its position
        if p==0:
            nums.append(target)
            nums.sort()
            for j in nums:
                if j==target:
                    p=nums.index(j)
                    
        return p
