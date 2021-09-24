/*
You are given an integer array nums. The adjacent integers in nums will perform the float division.
    For example, for nums = [2,3,4], we will evaluate the expression "2/3/4".
However, you can add any number of parenthesis at any position to change the priority of operations. You want to 
add these parentheses such the value of the expression after the evaluation is maximum.
Return the corresponding expression that has the maximum value in string format.
Note: your expression should not contain redundant parenthesis.

Example 1:
Input: nums = [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant, since they don't influence the operation priority. So you should return "1000/(100/10/2)".
Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2

Example 2:
Input: nums = [2,3,4]
Output: "2/(3/4)"

Example 3:
Input: nums = [2]
Output: "2"
*/





/*
Logic: [a,b,c...n] -> Answer will always be a/(b/c/.../n).

Why?
Let's use a little bit of observation and maths : Lets consider 2 cases

-> If we have something like 1000/100/10/2 without any parantheses then to evaluate the expression we start from 
beginning so 1000/100 reduces to 10 and expression becomes 10/10/2 which then reduces to 1/2 and finally to 
0.5. lets analysis another case
-> If we have parantheses everywhere like 1000/(100/(10/2)) so to evaluate this expression we start calculating 
from last (inner paranthese first) so this reduces to 1000/(100/5) then 1000/20 and finally to 50.
so from above two cases what we see is that if go like 1st case numerator start decreasing and so its final 
value but in second case numerator is as it is and denominator is decreasing that finally giving us a maimum 
value.

So for us to get largest value of the expression we want to maximize numerator and minimize denominator and 
thats why we will use 2nd way to keep maximum numerator and 1st way to minimize denomitor so this will look 
like 1000/(100/10/2) to remove confusion numerator is 1000 and denominator is (100/10/2).
*/
class Solution {
public:
    string optimalDivision(vector<int>& nums) {
        if(nums.size()==1)
            return to_string(nums[0]);
        if(nums.size()==2)
            return (to_string(nums[0])+"/"+to_string(nums[1]));
        
        string res="";
        for(int i=0;i<nums.size();i++){
            res+=to_string(nums[i])+"/";
            if(i==0)
                res+="(";
        }
        res.pop_back();
        res+=")";
        return res;
    }
};