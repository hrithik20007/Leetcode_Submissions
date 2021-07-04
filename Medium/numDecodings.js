/*
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). 
For example, "11106" can be mapped into:
    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The answer is guaranteed to fit in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0.
The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.
Hence, there are no valid ways to decode this since all digits need to be mapped.

Example 4:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
*/





/**
 * @param {string} s
 * @return {number}
 */
function decode(s,mem,i){
    var r1;
    if(s[i]=="0")
        return 0;
    if(i==s.length)
        return 1;
    if(i in mem)
        return mem[i];

    if(parseInt(s[i]+s[i+1])<=26 && i<=s.length-2){		//If the current consecutive two numbers are less than 27 and the current index is not at the last element
        r1=decode(s,mem,i+1)+decode(s,mem,i+2);
        mem[i]=r1;										//That is, stores the answer (as value) for the current index (as key).
    }
    else{
        r1=decode(s,mem,i+1);							//If we cannot the consecutive two numbers, since either it is >26 or if the current index is at the last element
        mem[i]=r1;
    }
    
    return r1;
}
    
var numDecodings = function(s) {
    var mem={}											//mem is a dictionary (or map) used for memoization. We take the indexes as key for whose solutions we know 
    													//and assign the number of solutions as the value. Thus, when that index is reached again, we simply return 
    													//the answer we know from the previous recursion(s). [Line 53]
    return decode(s,mem,0);
};





/*
Works but gives TLE error


function encode(s,k,l){
    if(s[0]=="0")
        return 0;
    if(k==l)
        return 1;
    if(k>l)
        return 0;
    
    var s1=s.substring(1);
    var s2=s.substring(2);
    if(parseInt(s[0]+s[1])>26)
        return encode(s1,k+1,l);
    else
        return encode(s1,k+1,l)+encode(s2,k+2,l);
}

var numDecodings = function(s) {
    var l=s.length;
    return encode(s,0,l);
};
*/
