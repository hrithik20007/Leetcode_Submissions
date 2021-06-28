/*
Every non-negative integer n has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except 
for n = 0, there are no leading zeroes in any binary representation.
The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary 
is "010" in binary.
For a given number n in base-10, return the complement of it's binary representation as a base-10 integer.

Example 1:
Input: n = 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

Example 2:
Input: n = 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.

Example 3:
Input: n = 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
*/




/**
 * @param {number} n
 * @return {number}
 */
var bitwiseComplement = function(n) {
    var s=n.toString(2);						//Converts the integer to base2 string (Meaning the string form of the integer in binary form)
    var r=[];									
    for(i=0;i<s.length;i++){
        s[i]=='1'?r.push('0'):r.push('1');		//Ternary operator to push the opposite digit into t
    }
    return parseInt(r.join(''),2);				//array.join(delimiter) joins a string by the delimiter. parseInt() converts that string into a decimal number.
    											//The base of the string number is given by the second parameter.
};
