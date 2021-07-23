/*
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
Given a balanced string s, split it in the maximum amount of balanced strings.
Return the maximum amount of split balanced strings.

Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Example 4:
Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
*/





/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    var c=0,p=0,q=0;

    for(i=0;i<s.length;i++){
        if(s[i]=='L')			//p keeps count of Ls
            p+=1;
        if(s[i]=='R')			//q keeps count of Rs
            q+=1;
        if(p==q){				//As soon as a balanced string is found, we increament c and reset p,q to start the counts anew
            c+=1;
            p=0;
            q=0;
        }
    }
    
    return c;
};
