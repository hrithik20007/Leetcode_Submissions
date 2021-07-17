/*
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
*/






/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 */
var countCharacters = function(words, chars) {
    var s,l=[],i,j,f=0;
    s=chars.slice();									//s stores a copy of chars (Changing s won't change chars)
    
    for(i of words){

        for(j of i){
            if(s.includes(j)){							//If the frequency of the characters in a word of words is less than or equal to that of s, then the word 
            											//is pushed to l
                var s1=s.indexOf(j);
                s=s.substring(0,s1)+s.substring(s1+1);	//If the character is found, then that is removed for the next iterations
            }
            else{
                f=1;
                break;
            }
        }

        if(f==0)										//That is, the word is valid as the loop was not broken mid-way
            l.push(i);
        else
            f=0;

        s=chars.slice();								//s again becomes chars (same as before)
    }

    return l.join('').length;							//Total length of all the valid words
};





/*
This works too but I wanted a faster solution



var countCharacters = function(words, chars) {
    var dc={},dw={},l=[],i,j,f=0;
    for(i of chars){
        if(i in dc)
            dc[i]+=1;
        else
            dc[i]=1;
    }
    
    for(i of words){
        for(j of i){
            if(j in dw)
                dw[j]+=1;
            else
                dw[j]=1;
        }
        for(j of i){
            if(j in dc && dc[j]>=dw[j])
                continue;
            else{
                f=1;
                break;
            }
        }

        if(f==0)
            l.push(i);
        else
            f=0;
        dw={};
    }

    return l.join('').length;
};
*/
