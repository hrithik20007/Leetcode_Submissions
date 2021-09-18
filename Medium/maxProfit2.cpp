/*
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and 
sell one share of the stock multiple times) with the following restrictions:
    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy 
again).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0
*/






/*Logic: Solved using State Machine Concept. Watch TechDose to fully grasp the concept.

cooldown state --> When I'm not holding any stock (Either sold the prev day or from cooldown the prev day)
hold state --> When I'm holding a stock (Either bought the current day or been holding from prev day)
sell state --> Selling stock today after holding from prev day
*/
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n=prices.size();
        if(n<=1)
            return 0;
        
        vector<int> cooldown(n,0), hold(n,0), sell(n,0);
        cooldown[0]=0;
        hold[0]=-prices[0];
        sell[0]=0;
        
        for(int i=1;i<n;i++){                               //Max profit of the states till the current day
            cooldown[i]=max(cooldown[i-1],sell[i-1]);
            hold[i]=max(hold[i-1],cooldown[i-1]-prices[i]);
            sell[i]=hold[i-1]+prices[i];
        }
        
        return max(cooldown[n-1],sell[n-1]);                //We do not hold stocks by the end, so that case is
                                                            //not considered
    }
};