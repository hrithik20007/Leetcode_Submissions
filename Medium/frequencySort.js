/*
Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
*/





/*
Logic: We first maintain a frequency dictionary. Then we make a list with its elements as [xi,yi], where xi is the frequency and yi is the key. We sort ths array in
descending order as per the frequencies. Then we use two for loops to add elements as per their frequencies to a resultant string r.
*/
/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    var i,j,r="",d={},l=[];
    for(i=0;i<s.length;i++){
        if(s[i] in d)
            d[s[i]]+=1;
        else
            d[s[i]]=1;
    }
    
    for(i in d)
        l.push([d[i],i]);
    l.sort((a,b)=>b[0]-a[0]);
    
    for(i=0;i<l.length;i++){
        for(j=0;j<l[i][0];j++){
            r+=l[i][1];
        }
    }
    
    return r;
};
