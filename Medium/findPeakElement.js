/*
A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
*/




/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {

    nums.unshift(-9999999999999999999999);		//Adding the cases of -infinity at the beginning and end
    nums.push(-9999999999999999999999);
    
    var l=1;
    var h=nums.length-2;
    while(h>=l){
        var mid=Math.trunc((h+l)/2);

        if(nums[mid+1]>nums[mid])				//In this case, we are certain to find a peak element after mid, so we increase l by 1.
            l=mid+1;

        else if(nums[mid-1]>nums[mid])			//  "     "    ....                  ......           before  ", so we decrease h by 1.     
            h=mid-1;

        else if(nums[mid-1]<nums[mid] && nums[mid]>nums[mid+1])			//We find peak element as the mid
            return mid-1;						//Since we added one element at the beginning, we would get the original index after decreasing mid by 1.
    }
    
    return l-1;									//We decrease l by 1 since     "     "
};
