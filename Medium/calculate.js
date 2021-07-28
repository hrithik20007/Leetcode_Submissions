/*
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
*/





/*
Logic: We put all the operands and operators in a list. Before inputting any operator, we input the operand before it and check the last operator that was input.
If the last operator was '-', we change the last operand to '- operand' and pop the '-' operator and normal operand. 
If the last operator was '/', we perform division on the last two operators and pop the last three elements. (2 operands and / opeartor). We then push the result.
We do the same for '*'.
If we encounter a '+', we do not input it into the list as we are going to add all the elements in the list anyway, at the end.
If we get a number string, we add the string numbers until we reach an operator. Otherwise if we have 22+3, then 2 and 2 will be stored separately.
Finally, we add the elements and return the result. 
*/
/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    var l=[],i,k="",k1;
    for(i of s){
        if(i==" ")
            continue;
        else if(i=='/' || i=='*' || i=='-' || i=='+'){
            k1=parseInt(k);
            l.push(k1);
            if(l[l.length-2]=="/"){
                k1=Math.trunc(l[l.length-3]/l[l.length-1])
                l.pop();
                l.pop();
                l.pop();
                l.push(k1);
            }
            else if(l[l.length-2]=="*"){
                k1=Math.trunc(l[l.length-3]*l[l.length-1])
                l.pop();
                l.pop();
                l.pop();
                l.push(k1);
            }
            else if(l[l.length-2]=="-"){
                l.pop();
                l.pop();
                l.push(-k1);
            }
            
            if(i!="+")
                l.push(i);
            k="";
        }
        else{
            k=k+i;
        }
    }


    
    k1=parseInt(k);
    l.push(k1);
    if(l[l.length-2]=="/"){
        k1=Math.trunc(l[l.length-3]/l[l.length-1])
        l.pop();
        l.pop();
        l.pop();
        l.push(k1);
    }
    else if(l[l.length-2]=="*"){
        k1=Math.trunc(l[l.length-3]*l[l.length-1])
        l.pop();
        l.pop();
        l.pop();
        l.push(k1);
    }
    else if(l[l.length-2]=="-"){
        l.pop();
        l.pop();
        l.push(-k1);
    }
    
    return l.reduce((a,b)=>a+b);
};






/*
Time Limit Exceeds



var calculate = function(s) {
    var l=[],i,k="",k1;
    for(i of s){
        if(i==" ")
            continue;
        else if(i=='/' || i=='*' || i=='+' || i=='-'){
            k1=parseInt(k);
            l.push(k1);
            if(l[l.length-2]=="/"){
                k1=Math.trunc(l[l.length-3]/l[l.length-1])
                l.pop();
                l.pop();
                l.pop();
                l.push(k1);
            }
            else if(l[l.length-2]=="*"){
                k1=Math.trunc(l[l.length-3]*l[l.length-1])
                l.pop();
                l.pop();
                l.pop();
                l.push(k1);
            }
            l.push(i);
            k="";
        }
        else
            k=k+i;
    }
    k1=parseInt(k);
    l.push(k1);
    if(l[l.length-2]=="/"){
        k1=Math.trunc(l[l.length-3]/l[l.length-1])
        l.pop();
        l.pop();
        l.pop();
        l.push(k1);
    }
    else if(l[l.length-2]=="*"){
        k1=Math.trunc(l[l.length-3]*l[l.length-1])
        l.pop();
        l.pop();
        l.pop();
        l.push(k1);
    }
    
    i=0;
    while(i<l.length){
        if(l[i]=="+"){
            k=Math.trunc(l[i-1]+l[i+1]);
            l.splice(i-1,3);
            l.splice(i-1,0,k);
            i-=1;
        }
        else if(l[i]=="-"){
            k=Math.trunc(l[i-1]-l[i+1]);
            l.splice(i-1,3);
            l.splice(i-1,0,k);
            i-=1;
        }
        i+=1;
    }
    
    return l[0];
};
*/






/*
Time Limit Exceeds



var calculate = function(s) {
    var i;
    var s1=s.split(" ").join('').split("+").join().split("-").join().split("*").join().split("/").join().split(",");
    
    for(i=0;i<s1.length;i++)
        s1[i]=parseInt(s1[i]);

    var l=[];
    for(i=0;i<s.length;i++){
        if(s[i]=='/' || s[i]=='*' || s[i]=='+' || s[i]=='-')
            l.push(s[i]);
    }
    //console.log(s1,l);
    var k,i=0;
    while(i<l.length){
        if(l[i]=="/"){
            k=Math.trunc(s1[i]/s1[i+1]);
            l.splice(i,1);
            s1.splice(i,2,k);
            i-=1;
        }
        else if(l[i]=="*"){
            k=Math.trunc(s1[i]*s1[i+1]);
            l.splice(i,1);
            s1.splice(i,2,k);
            i-=1;
        }
        i+=1;
    }
    //console.log(s1,l);
    i=0;
    while(i<l.length){
        if(l[i]=="+"){
            k=Math.trunc(s1[i]+s1[i+1]);
            l.splice(i,1);
            s1.splice(i,2,k);
            i-=1;
        }
        else if(l[i]=="-"){
            k=Math.trunc(s1[i]-s1[i+1]);
            l.splice(i,1);
            s1.splice(i,2,k);
            i-=1;
        }
        i+=1;
    }
    //console.log(s1,l);
    return s1[0];
};
*/
