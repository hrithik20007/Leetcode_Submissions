'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''



class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''
        This is my solution and it works. However, I wanted to look for a faster way.


        nums3=[]
        for i in nums1:
            if i in nums2 and i not in nums3:
                nums3.append(i)
                
        return nums3
        '''

        #The intersection method directly gives the intersecting elements between two SETS (not for lists or strings).
        return list(set(nums1).intersection(set(nums2)))
