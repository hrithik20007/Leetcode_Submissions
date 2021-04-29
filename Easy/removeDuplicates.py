#Remove duplicates from a sorted integer list and return the new list and its size

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        min=-2**64
        for i in nums[:]:
            if min<i:
                nums[c]=i
                c+=1
                min=i
            else:
                continue
            
        return c
        
        '''
        for i in nums[:]:
            p=i
            r=nums.index(i)
            for j in range(r+1,len(nums)):
                if p==nums[j]:
                    nums.remove(p)
        
        '''
