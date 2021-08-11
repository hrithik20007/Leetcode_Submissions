/*
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

Example 1:
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:
Input: n = 2
Output: [1,2]
*/





/*
Logic: Lexicographical order indicates dictionary order in alphabetical terms. In terms of numbers, the alphabets a->z are replaced by 0->9. Thus, 111 is smaller than 
2. 2034 is smaller than 3 and so on.
Here, we have used recursion to solve the problem. We start a for loop from 1->9. Then we call the function lexico for each of those numbers. Inside lexico, we start
another for loop for range [10i, 10i+9] (if i=1, then range becomes [10,19]). Then we do recursion for each of those numbers. If any of the numbers which are passed
into the function is greater than n, then we return. Thus never allowing our numbers to go above n. If it is below n, then we push the number into l.  
*/
/**
 * @param {number} n
 * @return {number[]}
 */
var lexicalOrder = function(n) {
    
    var l=[];
    function lexico(i){
        if(i>n)
            return;
        
        l.push(i);
        var a=i*10;
        var b=i*10+9;
        for(var k=a;k<=b;k++){
            lexico(k);
        }
    }
    
    for(var j=1;j<=9;j++){
        lexico(j);
    }
    
    return l;
};
