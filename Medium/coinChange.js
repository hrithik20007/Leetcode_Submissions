/*
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Example 4:
Input: coins = [1], amount = 1
Output: 1

Example 5:
Input: coins = [1], amount = 2
Output: 2
*/





//Watch Neetcode's video for detailed understanding.
/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    var dp=[],i,j;
    for(i=0;i<=amount;i++){
        dp[i]=amount+1;								//Initializing the array elements with maximum possible numbers
    }
    
    dp[0]=0;
    for(i=1;i<dp.length;i++){
        for(j of coins){
            if(i-j>=0){								//We take only those coins, which do not exceed the current value of the index of the dp array.
            										//For example, we cannot produce a sum of 3 by using a coin of value 6. 
                dp[i]=Math.min(dp[i],1+dp[i-j]);	//We add 1 to dp[i-j] to take account of the chosen j coin. For example, if I take a coin j of value 2 and i is 5.
                									//Then basically I'm adding the coin 2 to dp[3], which in turn shows the minimum coins to reach the value 3. So we 
                									//do- dp[3] + 1(for coin 2). 
            }
        }
    }
    
    if(dp[amount]==amount+1)
        return -1;
    else
        return dp[amount];
};
