/*
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
    Insert a character
    Delete a character
    Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
*/





/*
Logic: Watch TechDose for better understanding.

Cases-
1) Boundaries - If m has no characters, we insert n characters in it (n -> length of word2)
              - If n has no characters, we remove m characters from word1 (m -> length of word1).
2) If the current characters match - No change in number of operations from before (i.e. 1 char before of word1 
                and 1 char before of word2).
3) If characters don't match - 
Insert case - 1+dp[i][j-1], i.e. we go back one char of word2 to match the previous chars of word1 and word2.
Remove case - 1+dp[i-1][j], i.e. we go to the last char of word1 and match it with the current word2 char.
Replcase case - 1+dp[i-1][j-1], i.e. since we know the last two chars are equal, we decrease index of both for 
checking.
Then we take the minimum of these three cases.
*/
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m,n;
        m=word1.length();
        n=word2.length();
        
        int dp[m+1][n+1];
        int i,j;
        
        for(i=0;i<=m;i++)
            dp[i][0]=i;
        for(i=0;i<=n;i++)
            dp[0][i]=i;
        
        for(i=1;i<=m;i++){
            for(j=1;j<=n;j++){
                if(word1[i-1]!=word2[j-1])
                    dp[i][j]=min(1+dp[i-1][j-1],min(1+dp[i-1][j],1+dp[i][j-1]));
                else
                    dp[i][j]=dp[i-1][j-1];
            }
        }
        
        return dp[m][n];
    }
};