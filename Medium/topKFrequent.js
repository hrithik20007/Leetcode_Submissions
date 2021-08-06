/*
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
*/





//Note: I have done it in O(nlogn), but it was asked to do in a better time complexity.
//Logic: We store the character frequencies in a dictionary. We sort the frequencies after putting them in a list and find the k-th frequency from the end. Then
//we traverse the dictionary and find which keys have frequency greater than or equal to that frequency and push them into a list l1. At the end, we return l1. 
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    var i,l=[],d={};
    for(i=0;i<nums.length;i++){
        if(nums[i] in d)
            d[nums[i]]+=1;
        else
            d[nums[i]]=1;
    }
    
    for(i in d)
        l.push(d[i]);
    
    l.sort((a,b)=>a-b);
    
    var l1=[],n=l[l.length-k];
    for(i in d){
        if(d[i]>=n)
            l1.push(i);
    }
    
    return l1;
};
