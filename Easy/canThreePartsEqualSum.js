/*
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.
Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + 
arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

Example 1:
Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:
Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false

Example 3:
Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
*/






//Logic: We can simply check for the third of the total sum adding the items in sequence, because the partition will divide the array one after the other.
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var canThreePartsEqualSum = function(arr) {
    var r=0,c=0;
    var i,s=0;
    s=arr.reduce((a,b)=>a+b);				//The reduce() method executes a funtion while iterating over all the elements of an iterator, returning a single output 
    if(s%3!=0)
        return false;
    else{
        r=s/3;
        s=0;
    }
    for(let i of arr){      				//If we do (let i 'in' arr), then 'i' would represent the index rather than the array item (Same with var)
        s+=i;
        if(s==r){
            c+=1;
            s=0;
        }
        if(c==3)
            return true;
    }
    return false;
};




/*
The same code as above but in simpler terminology
var canThreePartsEqualSum = function(arr) {
    var r=0,c=0;
    var i,s=0;
    for(i=0;i<arr.length;i++){
        s+=arr[i];
    }
    if(s%3!=0)
        return false;
    else{
        r=s/3;
        s=0;
    }
    for(i=0;i<arr.length;i++){
        s+=arr[i];
        if(s==r){
            c+=1;
            s=0;
        }
        if(c==3)
            return true;
    }
    return false;
};
*/
