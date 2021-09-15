/*
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
*/






/*
Logic: Every even number's binary will have the same number of 1s as its half. Also, every odd number will have 
one more 1 in its binary than its previous number.
Intuition:

For odd numbers-
Eg: Let's consider 5.
4's binary -> 100
5's binary -> 101
(In even numbers, the rightmost bit will always be 0. But it is opposite in case of odd numbers. Alo note that
the rest of the bits remain same. Thus, 1s in 5 is one more than 1s in 4.)

For even numbers-
Eg: Let's consider 10.
5's binary -> 101
10's binary -> 1010
(We can see that the bits have left shifted by one place in order to obtain 10 from 5. We can think of it like-
5 -> (4+1)
10 -> 2(4+1) = (8+2)
Thus,the bits left shift by one place to enable 4 to 8 and 1 to 2. Hoever the number of 1s in both binaries 
remain same.)
*/
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(n+1,0);
        if(n==0)
            return ans;
        
        for(int i=1;i<=n;i++){
            if(i%2==0)
                ans[i]=ans[i/2];
            else
                ans[i]=ans[i-1]+1;
        }
        
        return ans;
    }
};




/*
This works as well.



class Solution {
public:
    int count_bit(int n){
        int s=0;
        while(n!=0){
            s+=n&1;
            n=n>>1;
        }
        return s;
    }
    
    vector<int> countBits(int n) {
        vector<int> ans;
        for(int i=0;i<=n;i++){
            ans.push_back(count_bit(i));
        }
        
        return ans;
    }
};
*/