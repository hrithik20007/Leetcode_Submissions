/*
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
*/





/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function(text) {
    var i,j=0,r=0,d={};
    for(i of text){
        if(i in d)
            d[i]+=1;
        else
            d[i]=1;
    }
    
    while(true){
        if('b' in d && d['b']>=1)
            d['b']-=1;
        else
            break;

        if('a' in d && d['a']>=1)
            d['a']-=1;
        else
            break;

        if('l' in d && d['l']>=2)
            d['l']-=2;
        else
            break;

        if('o' in d && d['o']>=2)
            d['o']-=2;
        else
            break;

        if('n' in d && d['n']>=1)
            d['n']-=1;
        else
            break;

        r+=1;						//If all the conditions are satisfied, then only we increase r, otherwise the loop breaks
    } 
    return r;
};
