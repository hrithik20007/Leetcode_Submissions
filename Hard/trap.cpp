/*
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much 
water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this 
case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
*/






/*
Logic: left and right vectors represent the maximum height of bar to the left and right of that particular index
respectively. While calculating ans, we calculate the maximum height of water that will be filled for that 
particular index, taking only the positive (>=0) answers. We do that by deducting the current bar height from
the minimum of the left and right maximum.
*/
class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> left(height.size(),0),right(height.size(),0);
        
        int lmax=height[0], rmax=height[height.size()-1];
        int i,ans=0;
        for(i=1;i<height.size();i++){
            lmax=max(lmax,height[i-1]);
            left[i]=lmax;
        }
        for(i=height.size()-2;i>=0;i--){
            rmax=max(rmax,height[i+1]);
            right[i]=rmax;
        }
        
        
        for(i=0;i<height.size();i++){
            ans+=max(min(left[i],right[i])-height[i],0);
        }
        
        return ans;
    }
};