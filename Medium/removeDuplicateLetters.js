/*
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order 
among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
*/





/*
Logic: We store the last indexes of all characters in a dictionary. While pushing elements into a list l, we pop the previous elements until the current element
to be inserted becomes smaller in lexicographical order, keeping in mind that they appear later in the string (we know this by seeing the last indexes of the 
characters from the dictionary). If it is already in lexicographical order, we can push the current element without popping any previous element.
*/
/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicateLetters = function(s) {
    var i,d={};
    for(i=0;i<s.length;i++)
        d[s[i]]=i;																//d stores the characters' last indexes
    
    var l=[];
    for(i=0;i<s.length;i++){
        if(!l.includes(s[i])){
            while(l.length>=1 && l[l.length-1]>s[i] && d[l[l.length-1]]>i)		//popping elements until in lexicographical order
                l.pop();
            l.push(s[i]);
        }
    }
    
    return l.join('');
};




/*
var removeDuplicateLetters = function(s) {
    var i=0,d={};
    s=s.split('');

    while(i<s.length){
        if(!(s[i] in d))
            d[s[i]]=1;
        else{
            s.splice(i,1);
            i-=1;
        }
        i+=1;
    }
    
    return s.sort().join('');
};
*/
