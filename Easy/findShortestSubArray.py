'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
'''





class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=Counter(nums)
        m=0
        f=0
        l=[]
        if len(list(set(nums)))==len(nums):     #All elements occur once, so its degree is 1
            return 1
        r=sys.maxsize
        for i in c.keys():
            if m<c[i]:
                m=c[i]      #m defines the degree of the array or the frequency of its most occuring element
        
        for i in c.keys():
            if c[i]==m:
                l.append(i)     #Multiple elements can have maximum frequency. Like maybe both 2 and 4 are present 3 times in the array (which is its degree).
        
        for p in l:
            for j in range(0,len(nums)):
                if f==0:
                    if nums[j]==p:  #For the first index of the most occuring element
                        i1=j
                        f+=1
                else:
                    if nums[j]==p:  #For the last index of the most occuring element
                        i2=j
            
            f=0
            r=min(r,len(nums[i1:i2+1]))     #We check the length of the subarray with the first index and last index of the most occuring elements. 
                
        return r


        '''
        Correct but time limit exceeded (Using recursion)


        def degree(self,nums,n):
            c=Counter(nums)
            m=0
            f=0
            for i in c.keys():
                m=max(m,c[i])

            if m<n:
                return 0

            p=self.degree(nums[1:],n)
            q=self.degree(nums[:len(nums)-1],n)

            if p==0 and q==0:
                return len(nums)

            if p==0 and q!=0:
                return q
            if p!=0 and q==0:
                return p

            return p    #In the default case where both p and q are equal

        def findShortestSubArray(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            c=Counter(nums)
            m=0
            f=0
            for i in c.keys():
                m=max(m,c[i])

            return self.degree(nums,m)
        '''



        '''
        c=Counter(nums)
        m=0
        f=0
        for i in c.keys():
            if m<c[i]:
                m=c[i]
                p=i
        
        for j in range(0,len(nums)):
            if f==0:
                if nums[j]==p:
                    i1=j
                    f+=1
            else:
                if nums[j]==p:
                    i2=j
                
        return len(nums[i1:i2+1])
        '''        
