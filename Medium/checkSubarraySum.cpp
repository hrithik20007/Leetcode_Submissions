/*
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false 
otherwise.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false
*/






/*
Logic:

It is easier to understand if you review a few concepts, so lets do that first:

A known property of mod: (a + b) % k = 0 is same as ((a % k) + (b % k)) % k = 0

something you can do in O(N), keep a running sum in some global. Lets call it currSum.

        int currSum = 0;
        for (int i = 0; i < nums.size(); i++) {
            currSum += nums[i];
		}

Now you have all the information you need to solve in O(N) time, but gotta do some math real quick. Your currSum above is relative to the start of the array at 
index 0. If you had stored(just to understand better) the currSum result into an array at each index of the loop in some array called sum[], then sum[x] would be 
sum of all numbers from index 0 to x.

Example:
sum[0] = nums[0]
sum[1] = nums[0] + nums[1]
sum[2] = nums[0] + nums[1] + nums[2]
sum[x] = nums[0] + nums[1] + nums[2] ... nums[x]

So far all of the above can be done in O(N) time in a single loop.
Now problem is asking if there exists any continous subarray where sum is multiple of k. Lets assume your continous subArray is from i to j, where i < j. Can you 
find any i, j where this is true?
Lets derive the sum of i to j from sum[] which we already calcluated in O(N) time.

sum(i,j) = sum[j] - sum[i] + nums[i] <---- Think about that a little bit and understand why this is true, very important!

Now what is the condition we are trying to solve for? Well we are trying to find any continous subarray sum such that sum(i,j) % k = 0. If you find any i, j where 
i<j then such a continous subarray exists.

sum(i,j) % k = 0 and if you sub the equation above you get:
(sum[j] - sum[i] + nums[i]) % k = 0

Now how do we rewrite the equation above so that it works with our single O(N) for loop. Well at each step of the for loop, your currSum global after being updated 
is sum[j]. So lets solve for the (sum[j] %k) term here. Remember the first rule of mod I showed at the start, use that to solve it.

(sum[j] % k) + ((nums[i] - sum[i]) % k) = 0
sum[j] % k = -1 * ((nums[i] - sum[i]) % k) <-----Final equation

Now look at your final equation and you will realize you have all the information at each step of that O(N) loop.

sum[j] % k: The sum[j] is just your currSum at each step in the loop, k is a known constant.
We will insert '-1 * ((nums[i] - sum[i]) % k)' in our map not knowing whether sum[j]%k for this exists or not. If we find sum[j]%k later, that means our original 
condition--> sum[j] % k = -1 * ((nums[i] - sum[i]) % k) is satisfied for a nums[i] and nums[j]. That means that such a subarray sum exists for which sum%k=0 and we 
return true. If we don't find it, we return false at the end.
*/
class Solution {
public:
    unordered_map<int,bool> mem;
    bool checkSubarraySum(vector<int>& nums, int k) {
        int i,s=0,temp;
        for(i=0;i<nums.size();i++){
            s+=nums[i];
            if(mem.find(s%k)!=mem.end())
                return true;
            
            temp=-1*((nums[i]-s)%k);
            mem[temp]=true;
        }
        
        return false;
    }
};






/*
class Solution {
public:
    unordered_map<pair<int,int>,int> mem;
    bool helper(int idx,int s,vector<int> &nums, int k,int c){
        if(s%k==0 && c>1)
            return true;
        if(idx==nums.size())
            return false;
        if(mem.count({idx,s})==1)
            return mem[{idx,s}];
        
        if(s>0)
            mem[{idx,s}]=helper(idx+1,s+nums[idx],nums,k,c+1);
        else
            mem[{idx,s}]=(helper(idx+1,s+nums[idx],nums,k,c+1)||helper(idx+1,s,nums,k,c));
        
        return mem[{idx,s}];
    }
    
    bool checkSubarraySum(vector<int>& nums, int k) {
        return helper(0,0,nums,k,0);
    }
};
*/
