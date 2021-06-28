#Return the index positions of two numbers in a list whose sum matches a given target

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=len(nums)
        for i in range(0,l-1):
            for j in range(i+1,l):
                aim=nums[i]+nums[j]
                if aim==target:
                    a=i
                    b=j
                    break
        return [a,b]

'''
target=int(input("Enter a target sum"))
nums=[]
n=int(input("Enter list size"))
for num in range(0,n):
    ele=int(input("Enter element no.: {0}".format(num)))
    nums.append(ele)

twoSum(nums,target)
'''
