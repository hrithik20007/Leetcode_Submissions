/*
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
*/





/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    var i,d={};
    var s=new Set();
    for(i of arr){
        if(i in d)
            d[i]+=1;			//Frequencies of the numbers are stored in d
        else
            d[i]=1;
    }
    
    var c=0;
    for(i in d){
        c+=1;					//c stores the length of the dictionary
        s.add(d[i]);			//set stores all the unique frequencies
    }
    
    if(s.size==c)				//If all the frequencies are unique, return true
        return true;
    else
        return false;
};
