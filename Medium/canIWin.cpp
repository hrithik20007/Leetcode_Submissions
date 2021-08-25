/*
In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 
wins.
What if we change the game so that players cannot re-use integers?
For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.
Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play 
optimally.

Example 1:
Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.

Example 2:
Input: maxChoosableInteger = 10, desiredTotal = 0
Output: true

Example 3:
Input: maxChoosableInteger = 10, desiredTotal = 1
Output: true
*/






class Solution {
    unordered_map<string,int>mp;
public:
    bool solve(string &nums , int t){
         if(mp.count(nums))return mp[nums];						//count returns 1 if nums is in dictionary, else 0 (Memoization)
         if(nums[nums.size()-1]-'0'>=t)return mp[nums]=true;	//If the last number in the string (representing the array) is greater than the total left
         for(int i=0; i<nums.size() ;i++){ 
               string cur =nums.substr(0,i)+nums.substr(i+1);  
                  if(!solve(cur,t-(nums[i]-'0'))){
                     return mp[nums]=true;						//The returning value toggles between true and false as we go up the recursion steps and at the 
                     											//uppermost step, it will give us whether the person with the first moves wins or loses
                  }
              }
        return mp[nums]=false;
    }
    bool canIWin(int num, int t) {
        if((num+1)*(num)/2<t)return 0;							//If the total of the numbers is less than the total to be reached
        if(t==0)return 1;										//If total is 0
        string nums="";        
        for(int i=1 ;i<=num ; i++)nums.push_back(i+'0');		//Making the array string
        return solve(nums,t);
    }
};
