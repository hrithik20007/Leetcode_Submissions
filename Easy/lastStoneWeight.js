/*
We have a collection of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:
    If x == y, both stones are totally destroyed;
    If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
*/





/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function(stones) {

    while(stones.length>1){
        stones.sort((a,b)=>a-b);
        a=stones[stones.length-1];			//a stores the largest stone weight
        b=stones[stones.length-2];			//b stores the second largest stone weight

        if(a-b==0){							//Both stones destroyed since same weight
            stones.pop();
            stones.pop();
        }
        else{								//Second largest stone destroyed and largest reduced to a-b
            stones.pop();
            stones.pop();
            stones.push(a-b);
        }
    }

    if(stones.length==1)
        return stones[0]
    else
        return 0							//In cases like [2,2]
};
