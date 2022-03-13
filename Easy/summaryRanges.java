/*
You are given a sorted unique integer array nums.
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each 
element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of 
the ranges but not in nums.

Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
*/







/*
Checking if the next value is 1 more than the current value. If yes, we make it a part of our current range,  
otherwise we just return the current element.
*/
class Solution {
    public List<String> summaryRanges(int[] nums) {
        ArrayList<String> res=new ArrayList<String>();
        
        int i=0,j;
        int a,b;
        while(i<nums.length){
            j=i+1;
            a=nums[i];
            b=nums[i];
            while(j<nums.length && nums[j]==nums[j-1]+1){
                b=nums[j];
                j+=1;
            }
            i=j;
            if(a==b)
                res.add(""+a);
            else
                res.add(""+a+"->"+b);
        }
        
        return res;
    }
}