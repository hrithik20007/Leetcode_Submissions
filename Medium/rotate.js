/*
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
*/




//nums.splice(-k) returns an array of the last k elements (due to the -ve sign) of nums array and the nums array is reduced to a an array without the last k characters. 
//func(...nums) is an ES6 operator called spread, which allows arguments in the parameter to be treated as an expandable iterator for the 'func' function.
//We then use that array as a parameter to pass into the unshift function to push those k elements at the front of the nums array.
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    k=k%nums.length;
    nums.unshift(...nums.splice(k*-1));
};




/*
var rotate = function(nums, k) {
    var i,j;
    k=k%nums.length;
    for(i=0;i<k;i++){
        j=nums.pop();
        nums.unshift(j);
    }
    
    return nums;
};
*/
