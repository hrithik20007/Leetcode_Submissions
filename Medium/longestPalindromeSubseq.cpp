/*
Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
*/







/*
Logic: Watch Pepcoding video to fully undertand the concept.
*/
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int dp[s.size()][s.size()];
        memset(dp,0,sizeof(dp));
        
        int len=0;
        for(int i=0;i<s.size();i++){
            int a=0;
            for(int j=i;j<s.size();j++){
                if(a-j == 0)
                    dp[a][j]=1;
                else{ 
                    if(s[a] == s[j])
                        dp[a][j]=2+dp[a+1][j-1];
                    else 
                        dp[a][j]=max(dp[a+1][j],dp[a][j-1]);
                }
                a+=1;
            }
        }
        
        return dp[0][s.size()-1];
    }
};
