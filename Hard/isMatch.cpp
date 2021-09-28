/*
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input: s = "acdcb", p = "a*c?b"
Output: false
*/






/*
Logic: Solved using 2D DP array. Rows indicate the string chars while column indicates the pattern chars.

dp[0][0] is true as both have 0 chars.

-> If the characters match or the pattern char is '?', which indirectly means that it also matches, then 
we see whether the strings, neglecting both the current chars from the string and pattern, had matched or not.
-> If the current char of the pattern is '*', then we see whether -
    - '*' means 0 string chars are considered (i.e. dp[i][j-1]).
    - '*' takes the current string char into its sequence (i.e. dp[i-1][j]).
    If either is true, then the current dp element is deemed true.
*/
class Solution {
public:
    bool isMatch(string s, string p) {
        int m=s.length();
        int n=p.length();
        
        int i,j;
        int dp[m+1][n+1];
        for(i=0;i<=m;i++){                  //By default, all dp elements are initialised as false
            for(j=0;j<=n;j++){
                dp[i][j]=false;
            }
        }
        
        dp[0][0]=true;
        
        for(i=1;i<=n;i++){                  //If we have '*' in the pattern for 0 chars in the original string
            if(p[i-1]=='*')
                dp[0][i]=dp[0][i-1];
        }
        
        for(i=1;i<=m;i++){
            for(j=1;j<=n;j++){
                if(s[i-1]==p[j-1] || p[j-1]=='?')
                    dp[i][j]=dp[i-1][j-1];
                else if(p[j-1]=='*')
                    dp[i][j]=dp[i-1][j] || dp[i][j-1];
            }
        }
        
        return dp[m][n];
    }
};