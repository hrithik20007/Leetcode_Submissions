'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #sys.maxsize gives the maximum value of Py_ssize_t(a typedef used internally in the implementation of CPython), depending upon the system architecture (It is the Python platform's pointer that dictates the maximum size of lists and strings)
        min_number=sys.maxsize
        max_profit=0
        
        # We compare the profits across multiple iterations and return the maximum profit. The min_number may become lesser after the highest number is crossed, but it dosen't matter because we are comparing the profit margin only via prices that come after that small price. Example = [2,6,1,4].. Here the profit won't be 6-1=5, but 6-2=4.
        for i in prices:
            min_number=min(min_number,i)
            profit=i-min_number
            max_profit=max(max_profit,profit)
            
        return max_profit
        
        '''
        p=10**5
        r=10**5
        q=-1
        for i in range(0,len(prices)):
            if p>prices[i]:
                p=prices[i]
                d=i

        #d=prices.index(p)

        f=0
        i=1
        while i<len(prices):
            if prices[i]>prices[i-1]:
                f=1
            i+=1

        if d==len(prices)-1:
            if f==0:
                return 0
            else:
                for i in prices[:d]:
                    if r>i:
                        r=i
                d=prices.index(r)
                p=r

        for j in prices[d+1:]:
            if q<j:
                q=j

        profit=q-p

        if profit>0:
            return profit
        else:
            return 0
        '''
