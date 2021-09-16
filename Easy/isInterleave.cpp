/*
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such 
that:
    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
*/






/*
Logic: We increase pointer i (for string s1) if s1[i] matches s3's current index, which is (i+j), i.e. the addition
of s1 and s2's current indexes. We do the same for pointer j in case of string s2. If s3's current index matches
both of that of s1 and s2, we increase both i and j in separate recursive function calls. The recursive function
has a base case such that we return true when both i and j reaches the end of s1 and s2 respectively. We use 
memoization to keep an account of the paths travelled. If any of the paths yeild true, then we return true, 
otherwise false.
*/
class Solution {
public:
    int dp[101][101];
    
    int helper(int i, int j, string s1, string s2,string s3){
        if(i==s1.length() && j==s2.length())
            return 1;
        if(dp[i][j]!=-1)
            return dp[i][j];

        int a=0,b=0;
        if(i<s1.length() && s1[i]==s3[i+j])
            a=helper(i+1,j,s1,s2,s3);
        if(j<s2.length() && s2[j]==s3[i+j])
            b=helper(i,j+1,s1,s2,s3);
        
        if(a||b)
            return dp[i][j]=1;
        else
            return dp[i][j]=0;
    }
    
    bool isInterleave(string s1, string s2, string s3) {
        if((s1.length()+s2.length())!=s3.length())
            return false;
        
        memset(dp,-1,sizeof(dp));
        return helper(0,0,s1,s2,s3);
    }
};







/*
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int i1=0,i2=0,j=0,s=0,f=0;
        while(j<s3.length()){
            while(s1[i1]==s3[j] && s2[i2]!=s3[j]){
                i1++;
                j++;
            }
            if(j>=s3.length())
                break;
            
            while(s1[i1]!=s3[j] && s2[i2]==s3[j]){
                i2++;
                j++;
            }
            if(j>=s3.length())
                break;
            
            if(s1[i1]==s3[j] && s2[i2]==s3[j])
                s=j;
            while(s1[i1]==s3[j] && s2[i2]==s3[j]){
                i2++;
                i1++;
                j++;
                if(s1[i1]!=s3[j])
                    f=1;
                else if(s2[i2]!=s3[j])
                    f=2;
            }
            if(f==1){
                i1=i1-(j-s);
                f=0;
            }
            if(f==2){
                i2=i2-(j-s);
                f=0;
            }
            if(j>=s3.length())
                break;
            
            if(s1[i1]!=s3[j] && s2[i2]!=s3[j])
                return false;
        }
        
        if(i1==s1.length() && i2==s2.length() && j==s3.length())
            return true;
        else
            return false;
    }
};
*/