/*
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next 
greater number. If it doesn't exist, return -1 for this number.

Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
*/






/*
Logic: Since this is a circular array, we can duplicate the array beyond the last element. Eg vector [1,2,1] will become [1,2,1,1,2,1]. We handle this using modulus.
Thus, element at index 4 becomes 4%(original size of array)=1. Thus we can compare the last elements to the initial elements like this. We put the elements' index 
into a stack and as soon as we find a larger element than the stack's top index's element, we put that larger element into the stack's top's index of the result 
vector and pop the index from the stack. When we don't find such larger elements later that means there is no larger element after it. So we cannot pop those elements.
In thsose cases, the resultant vector's indexes' value are not changed and remains -1 as we initialised it.
*/
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        stack<int> s;
        vector<int> ans(nums.size(),-1);
		int i,n=nums.size();
        
        s.push(0);
        for(i=1;i<2*n;i++){
            while(!s.empty() && nums[s.top()]<nums[i%n]){
                ans[s.top()]=nums[i%n];
                s.pop();
            }

            s.push(i%n);
        }
        
        return ans;
    }
};






/*
Brute Force Approach --> Works in O(n^2)


class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int i,j;
        vector<int> ans;
        
        for(i=0;i<nums.size();i++){
            j=i+1;
            while(j!=i){
                if(j==nums.size())
                    j=0;
                if(j==0 && i==0)
                    break;
                if(nums[i]<nums[j]){
                    ans.push_back(nums[j]);
                    break;
                }
                j+=1;
            }
            
            if(j==i)
                ans.push_back(-1);
        }
        
        return ans;
    }
};
*/
