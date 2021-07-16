/*
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
If multiple answers are possible, return any of them.
It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"

Example 4:
Input: numerator = 4, denominator = 333
Output: "0.(012)"

Example 5:
Input: numerator = 1, denominator = 5
Output: "0.2"
*/





/**
 * @param {number} numerator
 * @param {number} denominator
 * @return {string}
 */
var fractionToDecimal = function(numerator, denominator) {
    if(numerator%denominator==0)
        return (numerator/denominator).toString();
    
    var ans=Math.abs(Math.trunc(numerator/denominator)).toString();		//parseInt() can cause issue with huge -ve powers of 10. So, to obtain the integer portion
    																	//without the sign, I've used Math.trunc() and then Math.abs()
    if(numerator*denominator<0)
        var sign='-';													//For the sign
    else
        var sign='';
    
    var d={};
    var l=[ans,'.'];
    
    numerator=Math.abs(numerator);
    denominator=Math.abs(denominator);
    
    var r=numerator%denominator;
    
    while(r!=0){														//d stores the length of the list at which the recurring remainder occurs for the first time
    																	//and puts the '(' sign at that position. 
        if(r in d){
            l.splice(d[r],0,'(');
            l.push(")");
            break;
        }
        else{
            d[r]=l.length;
            r*=10;
            q=Math.trunc(r/denominator);
            r=r%denominator;
            l.push(q);
        }
    }
    
    return sign+l.join('');
};




/*
var fractionToDecimal = function(numerator, denominator) {
    var ans=(numerator/denominator).toString();
    if(!(ans.includes('.')))
        return ans;
    var a1=ans.split('.');
    var l=[];
    
    var s=parseInt(Math.sqrt(a1[1].length))+1;
    for(var i=1;i<=s;i++){
        if(a1[1].length%i==0 && i!=a1[1].length)
            l.push(i);
    }
    
    for(i of l){
        var s1=a1[1].substring(0,i);
        if(s1.repeat(a1[1].length/i)==a1[1]){
            a1[1]="("+s1+")";
            break;
        }
    }
    
    return a1.join('.');
};
*/
