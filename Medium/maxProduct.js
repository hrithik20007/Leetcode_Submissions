/*
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
It is guaranteed that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
*/





/**
 * @param {number[]} nums
 * @return {number}
 */
 //We keep a max and min variable to signify the maximum and minimum subarray product uptil that point (can be a single no. too). We do this because the next no.
 //may be positive or negative. If negative, then we get the max no. by multiplying with the min no. and vice-versa for a positive no.
 //We may encounter a 0 which will make the future products 0 as well. So we reset the max and min to 1 and calculate them after that 0. 
 //We also take note of the maximum max until that point as r, which we return at the end.
var maxProduct = function(nums) {
    var r=nums[0];
    var max=1,min=1,t;
    
    for(i of nums){
        if(i==0){
            max=1;
            min=1;
            t=min*i;
            min=Math.min(t,max*i,i);
            max=Math.max(t,max*i,i);
        }
        else{
            t=min*i;
            min=Math.min(t,max*i,i);
            max=Math.max(t,max*i,i);
        }
        r=Math.max(r,max);
    }
    return r;
};




/*
var maxProduct = function(nums) {
    var max=nums[0],p=1,arr=[1];
    for(i=1;i<=nums.length;i++){
        if(arr[i-1]==0)
            arr[i]=nums[i-1];
        else
            arr[i]=arr[i-1]*nums[i-1];
    }
    
    for(i=1;i<arr.length;i++){
        for(j=0;j<i;j++){
            if(arr[j]==0)
                continue;
            p=arr[i]/arr[j];
            if(p>max)
                max=p;
            console.log(i,j,max);
        }
    }
    console.log(arr);
    return max;
};
*/





/*
var maxProduct = function(nums) {
    var i=1,p=nums[0],max=nums[0];
    if(nums.length==1)
        return nums[0];
    while(i<nums.length){
        p*=nums[i];
        if(p>max)
            max=p;
        else
            p=nums[i];
        i+=1;
    }
    if(p>max)
        return p;
    else
        return max;
};
*/
