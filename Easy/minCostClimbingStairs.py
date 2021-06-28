'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].

Example 3:
Input: cost= [0,1,2,2]
Output: 2
Explaination: Cheapest is: start on cost[0], and then step on cost[2].
'''





class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        r=[0]*len(cost)
        r[0]=cost[0]
        r[1]=cost[1]
        for i in range(2, len(cost)):
            r[i]=cost[i]+min(r[i-1],r[i-2])
        return min(r[-1],r[-2])

        
        '''
        s=0
        i=0
        l=[]
        if len(cost)==2:
            return min(cost[0],cost[1])
        elif len(cost)==3:
            return min(cost[1],cost[0]+cost[2])
        else:
            a=cost[0]+cost[1]
            b=cost[1]+cost[2]
            c=cost[0]+cost[2]
            d=cost[1]+cost[3]
            l=[a,b,c,d]
            l.sort()
            if l[0]==a or l[0]==c:
                s+=cost[0]
            elif l[0]==b or l[0]==d:
                s+=cost[1]
                i=1

        while(i<len(cost)-2):
            if cost[i+1]<cost[i+2]:
                i+=1
                s+=cost[i]
            elif cost[i+1]>cost[i+2]:
                i+=2
                s+=cost[i]
            elif cost[i+1]==cost[i+2]:
                i+=2
                s+=cost[i]

        return s
        '''
