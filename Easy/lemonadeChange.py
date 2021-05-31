'''
At a lemonade stand, each lemonade costs $5. 
Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.
Note that you don't have any change in hand at first.
Return true if and only if you can provide every customer with correct change.

Example 1:
Input: [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:
Input: [5,5,10]
Output: true

Example 3:
Input: [10,10]
Output: false

Example 4:
Input: [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can't give change of $15 back because we only have two $10 bills.
Since not every customer received correct change, the answer is false.
'''





class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        d={5:0,10:0,20:0}
        if bills[0]==10 or bills[0]==20:
            return False
        for i in bills:
            if i==5:
                d[5]+=1
            if i==10:
                if d[5]>=1:
                    d[5]-=1
                    d[10]+=1
                else:
                    return False
            if i==20:
                if d[5]>=1 and d[10]>=1:
                    d[5]-=1
                    d[10]-=1
                    d[20]+=1
                elif d[5]>=3:
                    d[5]-=3
                    d[20]+=1
                else:
                    return False
                    
        return True
        
        
        '''
        t=[]
        if bills[0]==10 or bills[0]==20:
            return False
        for i in bills:
            if i==5:
                t.append(5)
            if i==10:
                if 5 in t:
                    t.remove(5)
                    t.append(10)
                else:
                    return False
            if i==20:
                if t.count(5)>=3:
                    t.remove(5)
                    t.remove(5)
                    t.remove(5)
                    t.append(20)
                elif 5 in t and 10 in t:
                    t.remove(10)
                    t.remove(5)
                    t.append(20)
                else:
                    return False
                    
        return True
        '''
