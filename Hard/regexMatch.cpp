/*
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' 
where:
    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
Input: s = "mississippi", p = "mis*is*p*."
Output: false
*/






/*
Logic: Watch NeatCode Video to fully grasp the concept.
*/
class Solution {
public:
    int dp[21][31];
    bool helper(int i, int j, string s, string p){
        if(i>=s.length() && j>=p.length())
            return true;
        if(j>=p.length())
            return false;
        if(dp[i][j]!=-1)
            return dp[i][j];
        
        bool match=(i<s.length() && (s[i]==p[j] || p[j]=='.'));
        if((j+1)<p.length() && p[j+1]=='*'){
            dp[i][j]=helper(i,j+2,s,p) || (match && helper(i+1,j,s,p));
            return dp[i][j];
        }
        if(match){
            dp[i][j]=helper(i+1,j+1,s,p);
            return dp[i][j];
        }   
        
        
        dp[i][j]=0;
        return false;
    }
    
    bool isMatch(string s, string p) {
        memset(dp,-1,sizeof(dp));
        return helper(0,0,s,p);
    }
};