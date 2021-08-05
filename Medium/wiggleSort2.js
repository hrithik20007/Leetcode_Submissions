/*
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
You may assume the input array always has a valid answer.

Example 1:
Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.

Example 2:
Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]
*/





//Time Complexity is O(nlogn) and space is of O(n) even though it is asked to do in O(n) and O(1) respectively.
//All the large numbers are placed in odd positions while it is opposite for even positions.
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var wiggleSort = function(nums) {
    var s=nums.slice();
    s.sort((a,b)=>a-b);
    var h=s.length-1,i=0;
    
    for(i=1;i<s.length;i+=2)
        nums[i]=s[h--];

    for(i=0;i<s.length;i+=2)
        nums[i]=s[h--];
};





/*
var wiggleSort = function(nums) {
    var i;
    for(i=1;i<nums.length;i+=2){
        if(i>0 && nums[i-1]>nums[i]){
            t=nums[i-1];
            nums[i-1]=nums[i];
            nums[i]=t;
        }
        if(i<nums.length-1 && nums[i+1]>nums[i]){
            t=nums[i+1];
            nums[i+1]=nums[i];
            nums[i]=t;
        }
    }
    
    return nums;
};
*/
