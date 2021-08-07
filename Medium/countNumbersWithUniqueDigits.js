/*
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

Example 1:
Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99

Example 2:
Input: n = 0
Output: 1
*/






/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    var i,j,s=0,l=[];
    l[0]=1;
    
    var d=0,nd=1;								//d denotes the duplicates while nd means non-duplicates (here the values are for n=0)
    for(j=1;j<=n;j++){							//We start checking for cases where n>=1
        d=d*10+nd*(j-1);						//Each digit containing duplicates will give 10 more duplicates in the next range (Example 22 can combined with [0,9]
        										//to give [220,229], all of which have duplicates). Also non duplicates like 12 can give (j-1) duplicates like 121 
        										//and 122.
        nd=Math.pow(10,j)-Math.pow(10,j-1)-d;	//Math.pow(10,j)-Math.pow(10,j-1) gives the number of numbers present in [10^(j-1),10^i). We deduct digits with 
     											//duplicates from that to get non-duplicate digits for that range.
        l.push(nd);
    }

    for(i=0;i<=n;i++)							//Summing the values of the array till n, as each array element represents the non-duplicates present in the range of
        s+=l[i];								//[10^(i-1),10^i), where i represents the index.
 
    return s;
};
