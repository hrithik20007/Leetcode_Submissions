/*
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.

Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
*/







/*
Logic: We make a min_list with the same number of elements as nums. The min_list[i] represents the minimum of all the numbers before nums[i]. min_list[0] is nums[0]
as there is no number before nums[0]. We start an iterator from the back of nums[i]. Think of it as i is going back in nums[i] as well as min_list. num[i]'s iterator
represents j while min_list's iterator represents i. Now we keep adding nums[i] into a stack which will give us k or the middle number. If at any point, the stack 
element becomes <=min_list[i], then we pop the elements from the stack until the last element becomes >min_list[i]. We do this because k must be greater than i.
When we find a nums[i](i.e. j) that is greater than the last element of stack, we know that will be k, as we already popped the elements smaller than i from the stack.
Thus it will be the condition i<k<j.  
*/
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int i,min=0,min_list[nums.size()];
        min_list[0]=nums[0];
        min=nums[0];
        for(i=1;i<nums.size();i++){
            min_list[i]=min;
            if(nums[i]<min)
                min=nums[i];
        }
        
        stack<int> st;
        for(i=nums.size()-1;i>=0;i--){
            if(nums[i] > min_list[i]){
                while(!(st.empty()) && st.top()<=min_list[i])
                    st.pop();
                
                if(!(st.empty()) && st.top()<nums[i])
                      return true;
                      
                st.push(nums[i]);
            }
        }
        return false;
    }
};








/*
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int i,a=INT_MAX,b=INT_MIN,c=INT_MIN;
        for(i=0;i<nums.size();i++){
            if(nums[i]<a)
                a=nums[i];
            else if(a<nums[i] && b<nums[i] && c<nums[i]){
                c=nums[i];
                //cout<<"C :"<<c<<" ";
            }
            else if(a<nums[i] && nums[i]<c){
                b=nums[i];
                //cout<<"B :"<<b<<" ";
            }
        }
        //cout<<c;
        if(a==INT_MAX || b==INT_MIN || c==INT_MIN)
            return false;
        else
            return true;
    }
};
*/
