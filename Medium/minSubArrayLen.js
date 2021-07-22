/*
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
*/





/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    var i,s=0,l=0,min=Number.MAX_SAFE_INTEGER;			//l works as the left pointer while i (the loop variable) acts as the right pointer
    for(i=0;i<nums.length;i++){

        s+=nums[i];

        while(s>=target){								//If the sum>=target, then we pop the beginning elements and increament l by 1. The sum may still remain
        												//>=target. Thus, by this method, we will keep track of the lengths between i and j and eventually we will
        												//find the smallest length.
            min=Math.min(min,i-l+1);
            s-=nums[l];
            l+=1;
        }
    }
    
    return (min!=Number.MAX_SAFE_INTEGER)? min : 0;
};





//Works but not fast enough 
/*
var minSubArrayLen = function(target, nums) {
    var i,min=Number.MAX_SAFE_INTEGER;
    for(i=0;i<nums.length;i++){
        var j=i,s=0;
        while(s<target && j<nums.length){
            s+=nums[j];
            j++;
        }
        
        if(!(j==nums.length && s<target)){
            var l=j-i;
            min=Math.min(l,min);
        }
    }
    
    if(min==Number.MAX_SAFE_INTEGER)
        min=0;
    return min;
};
*/




//Cumulative Approach -> O(n^2)   [Works but slow]
/*
var minSubArrayLen = function(target, nums) {
    var l=[0];
    for(i=1;i<nums.length+1;i++){
        l[i]=l[i-1]+nums[i-1];
    }
    
    var min=Number.MAX_SAFE_INTEGER;
    for(i=1;i<=l.length;i++){
        var s=0;
        for(j=0;j<=i;j++){
            s=l[i]-l[j];
            if(s>=target && i-j<min)
                min=i-j;
        }
    }
    
    if(min==Number.MAX_SAFE_INTEGER)
        min=0;
    return min;
};
*/
