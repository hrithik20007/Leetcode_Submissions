/*
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an 
empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise 
return -1. If there exists a solution, it is guaranteed to be unique

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
*/



/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    if(gas.reduce((a,b)=>a+b)<cost.reduce((a,b)=>a+b))			//That is, there can be no solution if the sum of cost is more than the sum of gas
        return -1
    
    var t=0,ans=0;												//If we reach this point, we are certain that there exists one solution garaunteed
    for(i=0;i<gas.length;i++){
        t+=gas[i]-cost[i];										//If t becomes -ve, it is turned to 0. However, the value of t can reduce (as long as it is >=0)
        														//over next iterations.
        
        if(t<0){
            t=0;
            ans=i+1;											//We are looking for that point starting fromm where the sum of the (gas-cost) is >=0. 
        }
    }
    return ans;
};
//It is important to note that when we discard the -ve values of (gas-cost) to 0, it may occur to us that the -ve values may have been greater than the net t 
//after all the iterations, but that wouldn't have been true as the sum(gas)>=sum(cost) condition prevents it from being so. That means t will always be >=0, no
//matter where it starts from. However, we are looking for that index starting from which t will never go below 0. 









/*
This works but takes more time as it is a brute force approach with time complexity of O(n^2).



var canCompleteCircuit = function(gas, cost) {
    var i,t,j,k,f=0;
    for(i=0;i<gas.length;i++){
        j=i+1;
        t=gas[i];
        if(j==gas.length)
            j=0;
        
        for(r=0;r<gas.length-1;r++){
            k=j-1;
            if(k==-1)
                k=gas.length-1;
            t=t-cost[k];
            if(t<0){
                f==2;
                break;
            }    
            t+=gas[j];
            j++;
            if(j==gas.length)
                j=0;
        }
        
        if(f!=2){
            k=j-1;
            if(k==-1)
                k=gas.length-1;
            t-=cost[k];
        }
        if(t>=0){
            f=1;
            break;
        }
    }
    if(f==1)
        return i;
    else
        return -1;
};
*/
