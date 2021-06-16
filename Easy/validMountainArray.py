'''
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true
'''




class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        f=0                             #f is changed to 1 when the array starts decreasing
        if len(arr)<3:
            return False
        if arr[1]<=arr[0]:              #To prevent a strictly decreasing array
            return False

        for i in range(2,len(arr)):
            if f==1 and arr[i]>=arr[i-1]:
                return False
            if f==0 and arr[i]<arr[i-1]:
                f=1
            if arr[i]==arr[i-1]:        #The elements cannot be equal in cases of strictly increasing or strictly decreasing
                return False
        
        if f==0:                        #To prevent a strictly increasing array
            return False
        else:
            return True
