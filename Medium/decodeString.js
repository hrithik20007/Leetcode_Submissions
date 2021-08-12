/*
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a 
positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be 
input like 3a or 2[4].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
*/






/**
 * @param {string} s
 * @return {string}
 */
function isNumeric(a){
    return /^-?\d+$/.test(a);
}

var decodeString = function(s) {
    var i,l=[];
    
    for(i=0;i<s.length;i++){
        if(s[i]!="]")
            l.push(s[i]);

        else{
            var s1="",s2="",k="";
            while(l.length>0 && l[l.length-1]!="[")					//Stores the string between the two brackets
                s1=l.pop()+s1;
            
            l.pop();
            while(l.length>0 && isNumeric(l[l.length-1])==true)		//Stores the number before the starting bracket
                k=l.pop()+k;
            k=parseInt(k);
            
            while(k>0){												//String s1 is multiplied k times to give s2
                s2+=s1;
                k-=1;    
            }
            
            l.push(s2);												//s2 is pushed to l
        }
    }
    
    return l.join('');			
};






/*
function isNumeric(a){
    return /^-?\d+$/.test(a);
}

var decodeString = function(s) {
    var l=[],k=[],i;
    for(i=0;i<s.length;i++){
        if(s[i]==="]"){
            var a=parseInt(l[l.length-3]);
            var s1=l[l.length-1];
            var r=s1;
            //console.log(i,a,s1,l);
            
            while(a>1){
                r+=s1;
                a-=1;
            }
            
            l.pop();
            l.pop();
            l.pop();
            l.push(r);
            //console.log(1,l);

            var s2="";
            while(l[l.length-1]!="[" && l.length>1)
                s2=l.pop()+s2;

            //console.log(s2);
            if(s2!="")
                l.push(s2);
            //console.log(2,l);
        }
        else if(s[i]!="[" && s[i]!="]" && isNumeric(s[i])==false){
            if(l[l.length-1]=="[" || l.length==0)
                l.push(s[i]);
            else
                l[l.length-1]+=s[i];
            console.log("bro",l);
        }
        else{
            l.push(s[i]);
            //console.log("Else",l);
        }
    }
    
    return l.join('');
};
*/
