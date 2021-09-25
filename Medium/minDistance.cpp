/*
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4
*/






/*
Logic: At first we found the length of largest common subsequence (LCS). Then we decrease that from both the
strings. The total of remaining lengths will give us the required answer.

To find the LCS -
A 2D dp array is used. Row side represents the characters of word1 while the column side does that of word2.
The first row and first column represents no characters. Since it is not possible to have common subsequences
with 0 characters from either strings, both the first row and column is filled with 0.
Now 2 cases arise for an i and j dp index. Either the characters match or they don't.

If they match-
We will add this character (length 1) to the LCS without taking the character from both the strings. That is,
to the diagonally left upper dp element.
If they don't match-
We take the maximum length of the LCS- one without taking the current word1 character and another without the
current word2 character. That is, either from the dp element from the row before or the column before. 
*/
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m=word1.length();
        int n=word2.length();
        int dp[m+1][n+1];
        
        int i,j;
        for(i=0;i<=m;i++)
            dp[i][0]=0;
        for(i=0;i<=n;i++)
            dp[0][i]=0;
        
        for(i=0;i<m;i++){
            for(j=0;j<n;j++){
                if(word1[i]==word2[j])
                    dp[i+1][j+1]=1+dp[i][j];
                else
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j]);
            }
        }
        
        return (m-dp[m][n])+(n-dp[m][n]);
    }
};