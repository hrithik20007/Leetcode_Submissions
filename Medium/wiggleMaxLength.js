/*
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one 
exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.
    For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
    In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is 
    not because its last difference is zero.
A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.
Given an integer array nums, return the length of the longest wiggle subsequence of nums.

Example 1:
Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).

Example 2:
Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length.
One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).

Example 3:
Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2
*/






/*
Logic: When the list elements wiggle, we only keep track of the peak elements (at the highest point and the lowest point). That way, we are taking into consideration
the extremes only and that allows more values to be less than (after the highest peak until a point) and more than (after the lowest peak until a point) the last 
peak. 
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var wiggleMaxLength = function(nums) {
    if(nums.length==1 || nums.length==2){
        if(nums.length==1)
            return 1;
        else{
            if(nums[0]==nums[1])
                return 1;
            else
                return 2;
        }
    }
    
    
    var i,c=0,l=[];									//c becomes 1 for decreasing, 2 for increasing and 0 if the first two elements are equal
    if(nums[1]<nums[0]){       						//decreasing at first
        c=1;
        l.push(nums[0])
    }
    else if(nums[1]>nums[0]){  						//increasing at first
        c=2;
        l.push(nums[0]);
    }

    
    for(i=1;i<nums.length-1;i++){
        if(c==1 && nums[i]<nums[i+1]){
            l.push(nums[i]);
            c=2;
        }
        else if(c==2 && nums[i]>nums[i+1]){
            l.push(nums[i]);
            c=1;
        }
        else{										//If the elements uptil now are equal
            if(c==0 && nums[i]<nums[i+1]){
                l.push(nums[i]);
                c=2;
            }
            
            else if(c==0 && nums[i]>nums[i+1]){
                l.push(nums[i]);
                c=1;
            }
        }
    }
    
    l.push(nums[nums.length-1]);					//Last element will always be a peak and thus, is pushed to the list
    
    return l.length;
};





/*
Works but time limit exceeds



var wiggleMaxLength = function(nums) {
    if(nums.length==1 || nums.length==2){
        if(nums.length==1)
            return 1;
        else{
            if(nums[0]==nums[1])
                return 1;
            else
                return 2;
        }
    }
    
    var mem={};
    
    function helper(idx,l){
        if(idx==nums.length){
            //console.log(l);
            return l.length;
        }

        var c=0;
        for(var i=idx;i<nums.length;i++){
            var l1=l.slice();
            if(l1.length<2 && l[l.length-1]!=nums[i])
                l1.push(nums[i]);
            else{
                if(l1[l1.length-1]-l1[l1.length-2]>0 && nums[i]-l1[l1.length-1]<0)
                    l1.push(nums[i]);
                else if(l1[l1.length-1]-l1[l1.length-2]<0 && nums[i]-l1[l1.length-1]>0)
                    l1.push(nums[i]);
                else if(l1[l1.length-1]==nums[i])
                    continue;
            }
            c=Math.max(c,helper(i+1,l1));
        }
        mem[idx]=c;
        return mem[idx];
    }
    
    return helper(0,[]);
};
*/
