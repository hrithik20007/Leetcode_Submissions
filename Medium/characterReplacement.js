/*
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this 
operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
*/





/*
Logic: See Neetcode's video for better understanding. Basically we are taking a window and counting the number of non-most frequent elements. If that exceeds k, we 
increase the left pointer. The substring between the right and left pointer gives the size of the result. 
*/
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    var maxf=0,res=0,d={};
    var l=0,r;
    
    for(r=0;r<s.length;r++){
        if(s[r] in d)
            d[s[r]]+=1;
        else
            d[s[r]]=1;
        
        maxf=Math.max(d[s[r]],maxf);
        while((r-l+1)-maxf>k){
            d[s[l]]-=1;
            l+=1;          
        }
        
        res=Math.max(res,r-l+1);
    }
    
    return res;
};
