/*
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.
Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers 
from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. 
The game ends when there are no more elements in the array.
Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume 
that both players are playing optimally.

Example 1:
Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.

Example 2:
Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
*/







/*
Logic: If there are even number of elements, player 1 will always find a way to win (By either starting at the odd end or even end, which has a greater total). 
If there are odd number of elements, then either player may win. We have used a helper recursive function to find that. If c is odd that means player 1 is playing,
otherwise player 2 is playing. For player 1, we have used || while selecting either the first or last element. That's because it will choose the path which will give
it true. If player 2 is playing, we used && because if player 2 finds even one false, it will try to go down that path and exploit it.
*/
class Solution {
public:
    bool helper(int sum1, int sum2, int n, int i, int c, vector<int>& nums){
        if(n<=i){
            if(sum1>=sum2)
                return  true;
            else
                return false;
        }
        
        if(c%2!=0)
            return helper(sum1+nums[i],sum2,n,i+1,c+1,nums) || helper(sum1+nums[n-1],sum2,n-1,i,c+1,nums);
        else
            return helper(sum1,sum2+nums[i],n,i+1,c+1,nums) && helper(sum1,sum2+nums[n-1],n-1,i,c+1,nums); 
    }    
    
    bool PredictTheWinner(vector<int>& nums) {
        if(nums.size()<=2)
            return true;
        if(nums.size()%2==0)
            return true;
        
        int i=0,j=nums.size()-1;
        return helper(0,0,nums.size(),0,1,nums);
    }
};
