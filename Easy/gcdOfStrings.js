/*
For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times)
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Example 4:
Input: str1 = "ABCDEF", str2 = "ABC"
Output: ""
*/





/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    const gcd=(a,b)=>{
        while(a%b!=0){
            var t=a%b;
            a=b;
            b=t;
        }
        return b;																		//Returns the hcf of the two string lengths
    }
    
    i=gcd(str1.length,str2.length);
    common=str1.substring(0,i);
    
    if(common.repeat(str1.length/i)==str1 && common.repeat(str2.length/i)==str2)		//str.repeat(n) returns a string repeating str 'n' times
        return common;
    else
        return "";
};





/*
This works but the above solution is simpler




var gcdOfStrings = function(str1, str2) {
    if(str1.length==str2.length){
        if(str1!=str2)
            return "";
        else
            return str1;
    }
    
    var i,j,f,s1,s2,l=[];
    if(str1.length>str2.length){
        s1=str1;
        s2=str2;
    }
    else{
        s1=str2;
        s2=str1;
    }

    for(i=s1.length;i>=1;i--){
        if(s1.length%i==0 && s2.length%i==0)
            l.push(i);
    }
    
    j=0,f=0;
    while(j<l.length){
        var s3=s1.substring(0,l[j]);
        for(i=l[j];i<s1.length;i+=l[j]){
           if(s1.substring(i,i+l[j])!=s3){
               f+=1;
               break;
           }
        }
        for(i=l[j];i<s2.length;i+=l[j]){
           if(s2.substring(i,i+l[j])!=s3){
               f+=1;
               break;
           }
        }

        if(f==0)
            return s3;
        else
            f=0;
        
        j+=1;
    }
    return "";
};
*/
