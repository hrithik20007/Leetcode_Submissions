/*
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the 
integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []
*/





/*
Logic: We use Math.abs(nums[i])-1 as index. We go to these indexes and mark their values -ve so as to say we have visited nums[i]. If we encounter the same index
again, it will contain a -ve value and we will know that nums[i] was repeated. So we push that into l and return l at the end. We use Math.abs() so as to use the 
values which have been converted into -ve by one of the previous nums[i].
*/
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    var i,l=[];
    for(i=0;i<nums.length;i++){
        if(nums[Math.abs(nums[i])-1]<0)
            l.push(Math.abs(nums[i]));
        else
            nums[Math.abs(nums[i])-1]=-nums[Math.abs(nums[i])-1];   
    }
    
    return l;
};





/*
var findDuplicates = function(nums) {
    var i=0,l=[];
    while(i<=nums.length){
        if(nums[i]==i+1)
            i+=1;
        else{
            var t=nums[i];
            nums.splice(i,1);
            if(nums[t-1]==t)
                l.push(t);
            nums.splice(t-1,0,t);
        }
        console.log(nums,l);
    }
    
    return l;
};
*/
