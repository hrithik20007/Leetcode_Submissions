/*
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
*/






/*
Logic: We remove the last element(s) only if the current element is smaller than the previous number(s) string.
*/
/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */
var removeKdigits = function(num, k) {
    if(num.length==k)
        return "0";
    
    var l=[num[0]];
    for(i=1;i<num.length;i++){
        if(num[i]<num[i-1] && k>0){
            while(l[l.length-1]>num[i] && k>0){
                l.pop();
                k-=1;
            }
        }
        l.push(num[i]);
    }
    
    while(k!=0){									//If k is not 0 yet
        l.pop();
        k-=1;
    }
    
    while(l[0]=="0" && l.length>1)					//Eliminating leading 0s
        l.shift();
    
    if(l.length==0)
        return "0";
    return l.join('');
};
