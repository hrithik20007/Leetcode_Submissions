'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        k=0
        #It is provided we can add the numbers from nums2 to nums1 itself as its size is actually n+m(the last ones being null initially)
        for i in range(m,m+n):
            nums1[i]=nums2[k]
            k=k+1
            
        return nums1.sort()
            
