/*
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:
Input: arr = [1,1]
Output: 1
*/





/**
 * @param {number[]} arr
 * @return {number}
 */
var findSpecialInteger = function(arr) {
    var i,c=1;								
    var n=parseInt(arr.length/4);		//The number frequency should be more than n (not equal to).
    if(c>n)
        return arr[0];					//If we have 3 or less elements in arr. In that case, we will have same three elements, as [1,2,3] will not have a
    									//unique answer and is an invalid testcase. Thus, if all three elements are same, then we can return the first one as answer.
    for(i=1;i<arr.length;i++){
        if(arr[i]!=arr[i-1])			//We use this approach as arr is sorted. Otherwise we would have used a dictionary.
            c=1;
        else{
            c+=1;
            if(c>n)
                return arr[i];
        }
    }
};
