/*
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
    0 <= i, j, k, l < n
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example 1:
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Example 2:
Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
*/






/*
Logic: We first find all the addition combinations of the first two arrays. Then we find the addition combinations of nums3 and nums4. If their -ve is present in 
the dictionary, then we add the frequency of such combinations to the count. Finally we return the count.
*/
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @param {number[]} nums4
 * @return {number}
 */
var fourSumCount = function(nums1, nums2, nums3, nums4) {
    var i,j,k,l,d={},c=0;
    
    for(i=0;i<nums1.length;i++){
        for(j=0;j<nums2.length;j++){
            if((nums1[i]+nums2[j]) in d)
                d[nums1[i]+nums2[j]]+=1;
            else
                d[nums1[i]+nums2[j]]=1;
        }
    }
    
    for(k=0;k<nums3.length;k++){
        for(l=0;l<nums4.length;l++){
            if(-(nums3[k]+nums4[l]) in d)
                c+=d[-(nums3[k]+nums4[l])];
        }
    }
    
    return c;
};
