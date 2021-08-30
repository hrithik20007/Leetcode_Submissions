/*
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.

Example 1:
Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Example 2:
Input: nums = [4,14,4]
Output: 4
*/






/*
Logic: We left shift 1 by 0-31 places and at each such place, we check the number of 1s and 0s of all the numbers in nums. For each such setbits and unsetbits values,
we will find the number of 0-1 and 1-0 combinations by doing unsetbits*setbits for that position. We repeat this for all positions and add the combinations. 
Finally we return the sum.   
*/
class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int i,j,ans=0;
        for(i=0;i<32;i++){
            int setbits=0;
            int unsetbits=0;
            
            for(j=0;j<nums.size();j++){
                if((nums[j]&(1<<i))!=0)
                    setbits+=1;
                else
                    unsetbits+=1;
            }
            ans+=(setbits*unsetbits);
        }
        
        return ans;
    }
};





/*
Brute Force --> Gives TLE


class Solution {
public:
    int countBits(int n){
        if(n==0)
            return 0;
        
        return (n&1)+countBits(n>>1);
    }
    
    int totalHammingDistance(vector<int>& nums) {
        int i,j,x,y,ans=0;
        for(i=0;i<nums.size()-1;i++){
            for(j=i+1;j<nums.size();j++){
                x=nums[i]^nums[j];
                ans+=countBits(x);
            }
        }
        
        return ans;
    }
};
*/
