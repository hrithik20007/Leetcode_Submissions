/*
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
*/





//Logic: Watch NeetCode Solution in YouTube to understand in detail. We have used a dp approach, similar to bottom-up in recursion.
/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    var dp=[];
    for(var i=0;i<nums.length;i++)
        dp.push(1);
    
    for(var i=nums.length-1;i>=0;i--){
        for(var j=i+1;j<nums.length;j++){
            if(nums[i]<nums[j])
                dp[i]=Math.max(dp[i],1+dp[j]);
        }
    }
    
    dp.sort((a,b)=>a-b);
    return dp[dp.length-1];
};




/*
var lengthOfLIS = function(nums) {
    
    var mem={};
    function subsequence(nums,idx,l,mem){
        if(idx==nums.length-1){
            mem[idx]=1;
            return mem[idx];
        }
        
        var maximum=0;
        for(i=idx;i<nums.length;i++){
            var l1=l.slice(),f=0;
            if(l1.length==0){
                f=1;
                l1.push(nums[i]);
                mem[idx]=1+subsequence(nums,i+1,l1,mem);
                l1.pop();
            }
            else{
                if(l1[l1.length-1]<nums[i]){
                    f=1;
                    l1.push(nums[i]);
                    mem[idx]=1+subsequence(nums,i+1,l1,mem);
                    l.pop();
                }
            }
            if(f==0 && i==nums.length-1)
                mem[idx]=1;
            
            maximum=Math.max(maximum,mem[idx]);
        }
        return maximum;
    }
    
    var x=subsequence(nums,0,[],mem);
    console.log(mem);
    return mem[0];
};
*/







/*
var lengthOfLIS = function(nums) {
    var ans=[],a,b;
    
    function subsequence(nums,idx,l){
        console.log("YO",idx);
        if(idx>=nums.length){
            ans.push(l.length)
            console.log("YOYO",ans);
            return 0;
        }
        
        for(i=idx;i<nums.length;i++){
            console.log("for",i);
            var l1=l.slice();
            if(l.length==0){
                console.log("A");
                l1.push(nums[i]);
                a=subsequence(nums,i+1,l1);
                l1.pop();
                b=subsequence(nums,i+1,l1);
            }
            else if(l.length!=0 && l[l.length-1]<nums[i]){
                console.log("B");
                l1.push(nums[i]);
                a=subsequence(nums,i+1,l1);
                l1.pop();
                b=subsequence(nums,i+1,l1);
            }
            
            if(a==0 && b==0)
                return 0;
        }
    }
    
    var x=subsequence(nums,0,[])
    
    console.log(ans);
    ans.sort((a,b)=>a-b);
    return ans[ans.length-1];
};
*/
