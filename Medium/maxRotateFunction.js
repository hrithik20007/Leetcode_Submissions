/*
You are given an integer array nums of length n.
Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:
    F(k) = 0*arrk[0]+1*arrk[1]+...+(n - 1)*arrk[n - 1].
Return the maximum value of F(0), F(1), ..., F(n-1).
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: nums = [4,3,2,6]
Output: 26
Explanation:
F(0) = (0* 4)+ (1 *3) + (2 *2) + (3 *6) = 0 + 3 + 4 + 18 = 25
F(1) = (0* 6)+ (1 *4) + (2 *3) + (3 *2) = 0 + 4 + 6 + 6 = 16
F(2) = (0* 2)+ (1 *6) + (2 *4) + (3 *3) = 0 + 6 + 8 + 9 = 23
F(3) = (0* 3)+ (1 *2) + (2 *6) + (3 *4) = 0 + 2 + 12 + 12 = 26
So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.

Example 2:
Input: nums = [100]
Output: 0
*/





/*
Logic:
Algo:
    Fully based on below observation
    Assume 3 elements [ a, b, c ]
    Calculate F(0) = 0xa + 1xb + 2xc
        Now come from reverse
            Caculate F(2), it is based on F(0)
            Similarly F(1) will be based on F(2)

Observation
// -----------------------
// a    b    c
// -----------------------
//                                  so sum = a+b+c
// -----------------------
//      b   2c      F(0)
// a   2b           F(1)    this is same as .. 3*b  -a-b-c(-sum)  + (2a+c)(F(2)) = 2b+a 		We actually multiply b with the no. of elements, which is 3 here
// 2a        c      F(2)    this is same as .. 3*a  -a-b-c(-sum)  + (b+2c)(F(0)) = 2a+c
// -----------------------
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxRotateFunction = function(nums) {
    if(nums.length==1)
        return 0;
    
    var n=nums.length;
    var max=Number.MIN_SAFE_INTEGER;
    var sum=nums.reduce((a,b)=>a+b);
    var i,j=0,r=0,k;
    for(i=0;i<n;i++){
        r+=nums[i]*j;
        j+=1;
    }
    max=Math.max(max,r);
    
    for(i=0;i<n-1;i++){
        r=(n*nums[i])+r-sum;
        max=Math.max(r,max);
    }
    
    return max;
};





/*
Time Limit Exceeds




var maxRotateFunction = function(nums) {
    if(nums.length==1)
        return 0;
    var sum=Number.MIN_SAFE_INTEGER;
    var i,j=0,r=0,k;
    for(i=0;i<nums.length;i++){
        r+=nums[i]*j;
        j+=1;
    }
    sum=Math.max(sum,r);
    
    
    for(i=nums.length-1;i>=1;i--){
        r=0;
        j=1;
        k=i+1;
        while(k!=i){
            if(k==nums.length)
                k=0;
            r+=nums[k]*j;
            k+=1;
            j+=1;
        }

        sum=Math.max(sum,r);
    }
    
    return sum;
};
*/
