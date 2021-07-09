/*
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
*/




/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
function recursion(s,words,idx,mem){
    if(idx==s.length)
        return true;
    if(idx in mem)
        return mem[idx];
    
    for(var i of words){
        var l=i.length;
        if(s.substring(idx,idx+l)==i){
            mem[idx]=recursion(s,words,idx+l,mem)
            if(mem[idx])
                return true;
        }
    }
    return false;
}

var wordBreak = function(s, wordDict) {
    return recursion(s,wordDict,0,{})
};





/*
var wordBreak = function(s, wordDict) {
    var i=0,j,sdict={},wdict={};
    while(i<wordDict.length){
        if(!(s.includes(wordDict[i]))){
            wordDict.splice(i,1);
            i-=1;
        }
        i+=1;
    }
    //console.log(wordDict);
    var word=wordDict.join('');
    
    for(j of word){
        if(j in wdict)
            wdict[j]+=1;
        else
            wdict[j]=1;
    }
    
    for(j of s){
        if(j in sdict)
            sdict[j]+=1;
        else
            sdict[j]=1;
    }
        
    for(j in sdict){
        if(j in wdict && wdict[j]<=sdict[j])
            continue;
        else
            return false;
    }
    return true;
};
*/
