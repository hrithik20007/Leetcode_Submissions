'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''



class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''
        This is my solution and it works but I wanted to make it faster.
        
        
        nums3=[]
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                nums3.append(i)
                
        return nums3
        '''

        '''
        Counter() produces key value pairs where the key represents the elements in the argument list and the value represents the frequency of that element in that list.
        '''
        c1=collections.Counter(nums1)
        c2=collections.Counter(nums2)
        s=[]
        
        for i in c1:
            s.extend([i]*min(c1[i],c2[i]))  #Here extends helps in extending a list with a no. of element from an iterable(like list, tuple, string etc.) which are appended at the end of the list. Here, an element is multiplied a no. of times and appended, as shown.
             
        return s
