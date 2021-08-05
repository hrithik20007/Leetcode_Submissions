/*
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.
On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, 
you only toggle the last bulb.
Return the number of bulbs that are on after n rounds.

Example 1:
Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 1
*/




/*
Logic: At first, all the bulbs are off. Then, we iterate from 1 to n and toggle the i-th bulb. Meaning -
At first, all bulbs will be switched on since they are multiples of 1, then bulbs which are present at positions which are multiples of 2 are toggled and so on.
If we see the pattern, only bulbs which have odd number of factors will remain on at the end. For example, 9 has factors - 1,3,9 (3->odd number), while 6 has factors -
1,2,3,6 (4->even number). We also notice that the numbers which have odd number of factors are perfect squares. Thus, we we will only count the number of perfect 
squares from 1 till n. Because the bulb will be switched on at those positions only, by the end. 
*/
/**
 * @param {number} n
 * @return {number}
 */
var bulbSwitch = function(n) {
    var i,c=0;
    for(i=1;i*i<=n;i++){
        c+=1;
    }
    
    return c;
};
