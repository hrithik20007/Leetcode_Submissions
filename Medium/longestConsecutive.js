/*
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
*/



/*
We convert the array into a set which makes it easier to see if an item is present or not. All the starting element of sequences have no element on their left on the
number line. Thus, when it dosen't have a left element, we can be sure it is the start of a sequence and we continue increasing its length, as long as there's an
element present on its right. At the end, we take the longest length of the sequences.
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    var numSet= new Set(nums);
    var l=0,longest=0;
    
    for(i of nums){
        if(numSet.has(i-1))
            continue;
        else{
            l=1;
            while(numSet.has(i+1)){
                l+=1;
                i+=1;
            }
            longest=Math.max(longest,l)
        }
    }
    return longest;
};
