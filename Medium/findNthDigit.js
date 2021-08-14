/*
Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

Example 1:
Input: n = 3
Output: 3

Example 2:
Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
*/





/*
Logic:
Formula to find total digits between range of single digits, double digits, triple digits, .... ∞
total digits = (higherbound - lowerbound + 1) digitlength

    Total digits between 1 => 9 : (9 - 1 + 1)* 1 = 9* 1 = 9
    Total digits between 10 => 99 : (99 - 10 + 1)* 2 = 90* 2 = 180
    Total digits between 100 => 999 : (999 - 100 + 1)* 3 = 900* 3 = 2700
    Total digits between 1000 => 9999 : (9999 - 1000 + 1)* 4 = 9000* 4 = 36000

Algo:
1. Find the range
2. Find the number
3. Find the digit
*/
/**
 * @param {number} n
 * @return {number}
 */
var findNthDigit = function(n) {
    let digits = 9, length = 1, res = 1;
  
    //1. Find the range
    while (n > digits * length) {
        n -= digits * length;
        length++;
        digits *= 10;
        res *= 10;
    }

    //2. Find the number
    res += (n - 1) / length;										//-1 for 0-indexing
    
    //3.Find the digit
    return parseInt(res.toString().charAt((n - 1) % length));		//Returns the digit at the remainder's index
};
