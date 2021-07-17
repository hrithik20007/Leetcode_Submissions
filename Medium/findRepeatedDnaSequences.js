/*
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
    For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return 
the answer in any order.

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
*/





/**
 * @param {string} s
 * @return {string[]}
 */
var findRepeatedDnaSequences = function(s) {
    if(s.length<10)
        return [];
    
    var d={},l=[];
    for(var i=0;i<=s.length-10;i++){
        var s2=s.substring(i,i+10);			//The strings' frequency is taken into account of by the dictionary d
        if(s2 in d)
            d[s2]+=1;
        else
            d[s2]=1;
    }
    
    for(i in d){
        if(d[i]>1)
            l.push(i);
    }
    return l;
};
