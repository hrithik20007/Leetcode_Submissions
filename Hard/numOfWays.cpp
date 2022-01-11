/*
Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree 
(BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder 
nums so that the constructed BST is identical to that formed from the original array nums.
For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array 
[2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.
Since the answer may be very large, return it modulo 109 + 7.

Example 1:
Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.

Example 2:
Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]

Example 3:
Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.
*/







/*
Logic:
It's a interesting math problem.
We will solve this problem by recursion, it's a little similar to dynamic programming.

On the top level, there is no doubt that nums[0] is the root of BST.
Remind that in BST, we have left < root < right.
Thus, those numbers who are smaller than nums[0], we put them in the vector left (which are the left children). And the 
others who greater than nums[0], we put them in vector right (which are the right children).
There are n position, index-0 is occupied by nums[0]. And we should put left in the remained n-1 positions, there are C[n-1][k] cases, where k is the length of left.

Remind the combination formula:
C[n][k] = C[n-1][k] + C[n-1][k-1]

Let f(nums) denote the number of cases, if we get the left, right vector mentioned above, then we can have:

f(nums) = f(left) * f(right) * C[n - 1][k]
where k is the length of left vector, and n is the length of vector nums.
*/

class Solution {
public:
    const int mod=(int)(1e9)+7;
    vector<vector<int>> C;
    
    int f(vector<int> nums){
        int n=nums.size();
        if(n<=1)
            return 1;
        
        vector<int> left,right;
        for(int i=1;i<n;i++){
            if(nums[0]<nums[i])
                right.push_back(nums[i]);
            else
                left.push_back(nums[i]);
        }
        
        int64_t l=f(left)%mod;
        int64_t r=f(right)%mod;
        return (((C[n-1][left.size()]*l)%mod)*r)%mod;
    }
    
    int numOfWays(vector<int>& nums) {
        int n=nums.size();
        C.resize(n,vector<int>(n,0));
        
        //Pascal's Triangle (does the job of C[n][k])
        for(int i=0;i<n;i++){
            C[i][0]=1;
            for(int j=1;j<=i;j++){
                C[i][j]=(C[i-1][j]+C[i-1][j-1])%mod;
            }
        }
        
        return f(nums)%mod-1;                               //-1 to exclude the vector in the question, i.e. nums
    }
};