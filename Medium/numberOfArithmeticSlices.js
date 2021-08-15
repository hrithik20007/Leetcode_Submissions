/*
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
    For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.
A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

Example 2:
Input: nums = [1]
Output: 0
*/





/*
Logic: We make a dp array of the same size as nums with all elements as 0. We take a three-element window and check whether the difference between the previous two 
and the two elements before that are same. If yes, we add 1+the previous dp element to the current index of the dp. 1 is added because the three element window make a
subarray that is an arithmetic sequence. We also add the previous dp element because this subarray will be a continious part of the previous elements if they also 
make a arithmetic sequence (as their difference will be equal to the first two elements of the current window). Finally we return the sum of the elements of dp array.
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfArithmeticSlices = function(nums) {
    if(nums.length<3)
        return 0;
    
    var dp=[],i;
    for(i=0;i<nums.length;i++)
        dp.push(0);
    
    for(i=2;i<nums.length;i+=1){
        if(nums[i-1]-nums[i-2]==nums[i]-nums[i-1])
            dp[i]=1+dp[i-1];
    }

    return dp.reduce((a,b)=>a+b);
};
