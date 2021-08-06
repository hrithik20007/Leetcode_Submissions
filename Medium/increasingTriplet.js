/*
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices 
exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
*/




//Note that by the end, the i-th value maybe after the j-th value, but it dosen't matter because at the end of the day there was a value less than j and we found a 
//value more than j.
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function(nums) {
    if(nums.length<3)
        return false;
    
    var n,i=Number.MAX_SAFE_INTEGER,j=Number.MAX_SAFE_INTEGER,k=Number.MAX_SAFE_INTEGER;
    for(n of nums){
        if(n<=i)			//Stores the smallest number 
            i=n;
        else if(n<=j)		//Larger than smallest
            j=n;
        else				//As soon as we find the number larger than j, we return true
        	return true;
    }
   	return false;
};
