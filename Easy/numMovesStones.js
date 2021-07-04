/*
Three stones are on a number line at positions a, b, and c.
Each turn, you pick up a stone at an endpoint (ie., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints.  
Formally, let's say the stones are currently at positions x, y, z with x < y < z.  You pick up the stone at either position x or position z, and move that stone to 
an integer position k, with x < k < z and k != y.
The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.
When the game ends, what is the minimum and maximum number of moves that you could have made?  Return the answer as an length 2 array: answer = [minimum_moves, 
maximum_moves]

Example 1:
Input: a = 1, b = 2, c = 5
Output: [1,2]
Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.

Example 2:
Input: a = 4, b = 3, c = 2
Output: [0,0]
Explanation: We cannot make any moves.

Example 3:
Input: a = 3, b = 5, c = 1
Output: [1,2]
Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.
*/




/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number[]}
 */
var numMovesStones = function(a, b, c) {
    var l=[a,b,c];
    l.sort((a,b)=>a-b);
    var r=[0,0];
    
    if(l[0]+1==l[1] && l[1]+1==l[2])			//When they are already consecutive
        return r;
    
    if(l[1]-l[0]<=2 || l[2]-l[1]<=2)			//For minimum moves. If the last 2 stones have one space between them, then the first stone can squeeze between them
    											//and if the last two stones are consecutive, we can move the first stone to the just before the second. So only 1 
    											//move is necessary.
        r[0]=1;
    else
        r[0]=2;									//Else 2 moves (similar to final else case, but we jump to those positions in this case, whereas we take single moves
        										//in that case)
    
    if(r[0]==1)
        r[1]=Math.abs(l[2]-l[0]-2);				//When minimum moves is 1
    else
        r[1]=(l[1]-l[0]-1)+(l[2]-l[1]-1);		//When we have to bring the first stone to just before the second one and the third stone to just after the second one
    
    return r;
};



/*
var l=[a,b,c];
l.sort((a,b)=>a-b);
a=l[0];
b=l[1];
c=l[2];
//console.log(a,b,c);
var min=0;
var max=0;
if(a!=b-1){
    console.log(min);
    min+=1;
    max+=(b-1)-a;
    console.log(min);
}
if(c!=b+1){
    console.log(min);
    min+=1;
    max+=c-(b+1);
    console.log(min);
}
return [min,max]
*/
