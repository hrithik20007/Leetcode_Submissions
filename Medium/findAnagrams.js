/*
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
*/






/*
Logic: We maintain a dictionary of the characters of p. We keep a count variable for the length of p. If all the values of keys match, we keep decreasing count. When 
it reaches 0, we push the left pointer's index to the list. When the substring length goes above p, we increase the left pointer; otherwise the right pointer is 
increased.
*/
/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    const l = [];
    const d = {};
    
    for (let i of p) {
        if (i in d) 
            d[i]++; 
        else 
            d[i] = 1;
    }
    
    let left = 0;
    let right = 0; 
    let count = p.length;

    while (right < s.length) {        
        if (d[s[right]] > 0) 
            count--;
    
        d[s[right]]--;
        right++;
        
        if (count === 0) 
            l.push(left);
         
        if (right - left == p.length) {
            if (d[s[left]] >= 0) 
                count++;
            d[s[left]]++;
            left++;
        }
    }
    return l;
};







/*
var findAnagrams = function(s, p) {
    var i,j=0,matched=0,d1={},d2={},l=[];
    for(i=0;i<p.length;i++){
        if(p[i] in d1)
            d1[p[i]]+=1;
        else
            d1[p[i]]=1;
    }
    //console.log(d1);
    d2=JSON.parse(JSON.stringify(d1));
    //console.log(d1,d2);
    for(i=0;i<s.length;i++){
        if(d2[s[i]]>0){
            d2[s[i]]-=1;
            if(d2[s[i]]==0)
                matched+=1;
        }
        else{
            j=i;
            d2=JSON.parse(JSON.stringify(d1));
        }
        console.log(i,d2,matched);
        if(matched==p.length){
            l.push(j);
            matched=0;
            d2=JSON.parse(JSON.stringify(d1));
        }
    }

    return l;
};
*/
