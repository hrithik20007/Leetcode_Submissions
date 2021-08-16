/*
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets 
is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
*/







/*
Logic: We move towards each nums element and either include it in a new array (decrease its value from our target) or not. If we reach the target we return true.
*/
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function(nums) {
    var mem={};
    var s=nums.reduce((a,b)=>a+b);
    if(s%2!=0)
        return false;
    var target=Math.trunc(s/2);						//Target must be half of the total sum
    
    function partition(idx,target){
        if(target==0)
            return true;
        if(idx,target in mem)						//Memoization
            return mem[idx,target];
        if(target<0 || idx==nums.length)
            return false;
        
        var c1=partition(idx+1,target-nums[idx]);	//We include the current element
        var c2=partition(idx+1,target);				//We don't include the current element
        
        if(c1||c2)									//If either c1 or c2 return true
            mem[idx,target]=true;
        else
            mem[idx,target]=false;
        
        return mem[idx,target];
    }
    
    return partition(0,target);
};







/*
Works but time limit exceeds



var canPartition = function(nums) {
    var mem={};
    var s=nums.reduce((a,b)=>a+b);
    if(s%2!=0)
        return false;
    
    function partition(idx,l,s1,s2){
        if(s1==s2)
            return true;
        
        var r;
        for(var i=idx;i<nums.length;i++){
            if(s2+nums[i]<=s1-nums[i]){
                l.push(nums[i]);
                r=partition(i+1,l,s1-l[l.length-1],s2+l[l.length-1]);
                l.pop();
            }
            if(r==true)
                break;
        }
        
        if(r==true)
            return true;
        else
            return false;
    }
    
    return partition(0,[],s,0);
};
*/




/*
var canPartition = function(nums) {
    nums.sort((a,b)=>a-b);
    var s1=nums.reduce((a,b)=>a+b);
    
    var l=[],s2=0;
    while(s2<s1){
        l.push(nums.pop());
        s2+=l[l.length-1];
        s1-=l[l.length-1];
    }
    
    if(s1==s2)
        return true;
    else
        return false;
};
*/
