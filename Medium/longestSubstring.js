/*
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or 
equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
*/






/*
Logic: The solution works by the divide and conquer algorithm. We find out the frequencies of all the characters in the string and keep track of the ones which appear
less than k times. We divide the string into substrings when we encounter such a character - one from the start till before it and another after it till the end.
We take the maximum length of the substring out of these two, which dosen't have any such characters. If we dont encounter such a character, then we simply return 
the length of that string. We do all this by recursion and at the top level, we will get our required length.
*/
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubstring = function(s, k) {
    
    function divideandconquer(start,end){
        var i,j,d={};
        for(i=start;i<end;i++){
            if(s[i] in d)
                d[s[i]]+=1;
            else
                d[s[i]]=1;
        }
        
        for(j=start;j<end;j++){
            if(d[s[j]]<k){
                var c1=divideandconquer(start,j);
                var c2=divideandconquer(j+1,end);
                return Math.max(c1,c2);
            }
        }
        return end-start;
    }
    
    return divideandconquer(0,s.length);
};






/*
var longestSubstring = function(s, k) {
    var d={},i,j,c=0,r=0;
    for(i=0;i<s.length;i++){
        if(s[i] in d)
            d[s[i]]+=1;
        else
            d[s[i]]=1;
    }
    
    for(j=0;j<s.length;j++){
        if(d[s[j]]>=k)
            c+=1;
        else{
            r=Math.max(c,r);
            c=0;
        }
    }
    
    if(r==0)
        return c;
    else
        return r;
};
*/
