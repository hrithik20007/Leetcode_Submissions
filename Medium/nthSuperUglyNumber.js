/*
A super ugly number is a positive integer whose prime factors are in the array primes.
Given an integer n and an array of integers primes, return the nth super ugly number.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

Example 1:
Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].

Example 2:
Input: n = 1, primes = [2,3,5]
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].
*/






/*
Logic: Similar to nthUglyNumber. In that problem we had a fixed set of prime numbers -> 2,3 and 5. Here, we have a list of those primes. Basically the overall concept
remains the same. We choose the smallest factor of the primes in the given list each time and add it to the list. If the factor was of 2 (say), then we increase the
dictionary value of 2 by 1. This ensures that the pointer to the lowest factor now moves by 1 place, such that we get the next lowest possible factors available to us
from which we choose the minimum. This helps maintain the increasing sequence of ans and all the values input are the n lowest factors possible.
*/
/**
 * @param {number} n
 * @param {number[]} primes
 * @return {number}
 */
var nthSuperUglyNumber = function(n, primes) {
    var ans=[1],i,d={};
    for(i of primes){
        d[i]=0;									//Keeps track of the pointers of the prime numbers
    }

    var min=Number.MAX_SAFE_INTEGER;
    while(ans.length<n){
        for(i of primes)
            min=Math.min(min,ans[d[i]]*i);
        ans.push(min);							//Current minimum factor available at our disposal is pushed to ans
        
        for(i of primes){
            if(min==ans[d[i]]*i)
                d[i]+=1;
        }
        
        min=Number.MAX_SAFE_INTEGER;			//Resets min for the next iteration
    }
    
    return ans[ans.length-1];
};
