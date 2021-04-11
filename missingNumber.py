class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        nums.sort()
        if nums[n-1]==n-1:
            return n
        elif nums[0]!=0:
            return 0
        else:
            k=0
            for i in range(0,n):
                if nums[i]!=k:
                    s=k
                k+=1
            return s
