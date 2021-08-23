/*
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
In one move, you can increment or decrement an element of the array by 1.
Test cases are designed so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Example 2:
Input: nums = [1,10,2,9]
Output: 16
*/





/*
Logic: We change all the numbers to the median value of nums. Median is a more accurate representation of a medium value for skewed data or data which has outliers 
(which is a point whose deviates from the rest by a large amount). Mean is more appropriate for normal data distribution.
*/
class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int i,c=0;
        int median=nums[(0+nums.size()-1)/2];
        for(i=0;i<nums.size();i++)
            c+=abs(median-nums[i]);
        
        return c;
    }
};





/*
We need median, not mean

class Solution {
public:
    int minMoves2(vector<int>& nums) {
        int i,j,c=0,s=0,s1;
        for(i=0;i<nums.size();i++){
            s+=nums[i];
        }
        s1=(int)(s/nums.size());
        
        for(j=0;j<nums.size();j++){
            if(s1==nums[j])
                continue;
            
            else if(nums[j]<s1)
                c+=s1-nums[j];
            else
                c+=nums[j]-s1;
        }
        
        return c;
    }
};
*/
