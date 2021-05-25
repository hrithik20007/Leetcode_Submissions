class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    
        l=0
        h=len(nums)-1
        
        while(l<h):
            mid=(l+h)//2

            if nums[mid]==target:
                return mid

            elif nums[mid]>nums[l]:     #Checking if the left side of mid is in sorted order
                if nums[l]<=target<=nums[mid]:  #If the target is within the left side's sorted range
                    h=mid
                else:
                    l=mid+1
                                    
            else:                       #If not, then the right side is definitely in sorted order
                if nums[mid+1]<=target<=nums[h]:    #If the target is within the right side's sorted range
                    l=mid+1
                else:
                    h=mid  
        

        if nums[l]==target:     #At this point, h and l are equal, so we can write either nums[h] or nums[l]. In while, we have not used equal to
                                #as the loop will continue and if a number is given that is not present, then (h+l)//2!=target and as h or l is
                                #changed, then an index error may be shown
            return l
        else:
            return -1

            
    '''
    I decided against this solution because it uses sorted() function which has a time complexity of nlogn while we need a log n time complexity.


    
    def binarysearch(self,l1,l2,nums,target):
        while(l1<=l2):
            mid=(l1+l2)//2
            if nums[mid]==target:
                return mid
                break
            elif nums[mid]>target:
                l2=mid-1
            else:
                l1=mid+1
        return -1
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=min(nums)
        n1=sorted(nums)[0]
        if n1!=0:
            l1=0
            l2=n1-1
            l3=n1
            l4=len(nums)-1
            if target>=nums[l1]:
                return self.binarysearch(l1,l2,nums,target)
            else:
                return self.binarysearch(l3,l4,nums,target)
        else:
            l1=0
            l2=len(nums)-1
            return self.binarysearch(l1,l2,nums,target)
    '''
