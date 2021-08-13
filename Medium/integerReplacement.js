/*
Given a positive integer n, you can apply one of the following operations:
    If n is even, replace n with n / 2.
    If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

Example 1:
Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1

Example 2:
Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1

Example 3:
Input: n = 4
Output: 2
*/






/**
 * @param {number} n
 * @return {number}
 */
var integerReplacement = function(n) {
    var mem={};
    
    function replace(k){
        if(k==1)												//Base Case
            return 1;
        else if(k in mem)										//Memoizatiom
            return mem[k];
        else if(k==0)											//Either c1,c2 or c3 from the previous step was not updated. Thus, this path will be avioded at all
            return Number.MAX_SAFE_INTEGER;						//costs. Thus we return the max number possible to avoid this path.
        
        var c1=0,c2=0,c3=0;
        if(k%2==0)
            c1=Math.trunc(k/2);
        else{
            c2=k+1;
            c3=k-1;
        }

        mem[k]=1+Math.min(replace(c1),replace(c2),replace(c3));	//We will preferably take the combination with the lesser steps
        return mem[k];
    }
    
    return replace(n)-1;
};
