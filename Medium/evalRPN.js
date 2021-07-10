/*
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by 
zero operation.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1)*3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10* (6 / ((9 + 3)* -11))) + 17) + 5
= ((10*(6/(12* -11))) + 17) + 5
= ((10*(6/ -132)) + 17) + 5
= ((10*0)+17) + 5
= (0+17) + 5
= 17 + 5
= 22
*/





/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    var i,l=[];
    for(i=0;i<tokens.length;i++){
    
        if(tokens[i]=='/'){
            var r=parseInt(l[l.length-2])/parseInt(l[l.length-1]);		//parseInt converts the string characters into integers
            l.pop();
            l.pop();
            l.push(Math.trunc(r));										//Math.trunc() deletes the decimal part of a number (takes only the integer part)
        }
        
        else if(tokens[i]=='*'){
            var r=parseInt(l[l.length-2])*parseInt(l[l.length-1]);		//We perform the operation on the last two numbers, so they are popped and the result is pushed
            l.pop();
            l.pop();
            l.push(Math.trunc(r));
        }
        
        else if(tokens[i]=='-'){
            var r=parseInt(l[l.length-2])-parseInt(l[l.length-1]);
            l.pop();
            l.pop();
            l.push(Math.trunc(r));
        }
        
        else if(tokens[i]=='+'){
            var r=parseInt(l[l.length-2])+parseInt(l[l.length-1]);
            l.pop();
            l.pop();
            l.push(Math.trunc(r));
        }
        else
            l.push(tokens[i]);
    }
    return l[0];
};
