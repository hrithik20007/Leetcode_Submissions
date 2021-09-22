/*
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is 
considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:
    perm[i] is divisible by i.
    i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

Example 1:
Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1

Example 2:
Input: n = 1
Output: 1
*/





/*
Logic: We use recursion to continue down the paths which statisfy either of the two conditions, otherwise we 
return. If we can traverse all the numbers down a particular path - from 1 to n, then we increase the count 
by 1.
*/
class Solution {
public:
    void helper(int n, int idx, vector<bool> &visited, int &c){
        if(idx>n) c+=1;
        
        for(int i=1;i<=n;i++){
            if(!visited[i] && (idx%i==0||i%idx==0)){
                visited[i]=true;
                helper(n,idx+1,visited,c);
                visited[i]=false;
            }
        }
    }
    
    int countArrangement(int n) {
        vector<bool> visited(n+1,false);
        int c=0;
        helper(n, 1, visited, c);
        return c;
    }
};