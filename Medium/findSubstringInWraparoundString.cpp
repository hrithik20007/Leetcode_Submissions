/*
We define the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this:
    "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
Given a string p, return the number of unique non-empty substrings of p are present in s.

Example 1:
Input: p = "a"
Output: 1
Explanation: Only the substring "a" of p is in s.

Example 2:
Input: p = "cac"
Output: 2
Explanation: There are two substrings ("a", "c") of p in s.

Example 3:
Input: p = "zab"
Output: 6
Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab") of p in s.
*/





/*
Logic: It is important to note that we only take into account the subarrays and not the rest of the subsequences of p. When we move from left to right, the first
character will always be valid. So we change the value at that character's index in the dp vector to 1. If the next character is 1 more in ASCII value than the 
previous or is A after the previous Z, then we have two new valid substrings -> one the last character and the another the first two characters combined. So, we
increase the count by 1 to give 2. We make the value at this new character's index in dp vector 2. Now if we think we have had 3 possible valid combinations.
The two characters alone and one which combines them both. We can get this by adding 1 and 2 after iterating through the dp vector. We use this same logic for larger
strings of p.
Also take note that we used max of dp[index[i]] and count. It is because when we reach the same character, say a, then it will likely be followed by b,c and so on.
Thus , we use this to avoid duplicate strings (with same starting characters).
*/
class Solution {
public:
    int findSubstringInWraproundString(string p) {
        vector<int> dp(26,0);												//dp array contains 26 elements, all initialised to 0
        int i,count=1,s=0;
        vector<int> index;
        
        for(i=0;i<p.length();i++)
            index.push_back(int(p[i])-97);									//Holds the alphabetic integer value of p's characters from 0-25

        for(i=0;i<p.length();i++){
            if(i>0 && (index[i]-1==index[i-1] || index[i]+25==index[i-1]))
                count+=1;
            else
                count=1;													//A new subarray will be counted from this point
            
            dp[index[i]]=max(dp[index[i]],count);
        }
        
        for(i=0;i<dp.size();i++)											//Adding the values of the dp vector
            s+=dp[i];
        
        return s;
    }
};







/*
In this sum, I took into account the subsequences instead of the subarrays only.



class Solution {
public:
    void substring(string ans,int idx, vector<string> &l, string p){
        if(idx>=p.length()){
            if(find(begin(l),end(l),ans)==end(l) && ans!="")
                l.push_back(ans);
            return;
        }
        
        substring(ans+p[idx],idx+1,l,p);
        substring(ans,idx+1,l,p);
    }
    
    int findSubstringInWraproundString(string p) {
        vector<string> l;
        substring("",0,l,p);
    
    int i,j,c=0,f=0;
    //copy(l.begin(),l.end(),ostream_iterator<string>(cout," "));
    //cout<<l.size()<<endl;
    for(i=0;i<l.size();i++){
        for(j=1;j<l[i].length();j++){
            if(int(l[i][j])==int(l[i][j-1])+1)
                continue;
            else{
                if(int(l[i][j])==97 && int(l[i][j-1])==122)
                    continue;
                else{
                    f=1;
                    break;
                }
            }
        }
        
        if(f!=1){
            //copy(l.begin(),l.end(),ostream_iterator<string>(cout," "));
            //cout<<c<<" "<<i<<endl;
            c+=1;
        }
        else
            f=0;
    }
        
    return c;
    }
};
*/
