/*
Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.
An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.
A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
    For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include 
    "aebdc", "aeb", and "" (empty string).

Example 1:
Input: strs = ["aba","cdc","eae"]
Output: 3

Example 2:
Input: strs = ["aaa","aaa","aa"]
Output: -1
*/






/*
Logic: We start two for loops to check two strings from the same given list at once. If they are same or if strs[i] is equal to the first 'strs[i].length()' alphabets
of strs[j], then we convert a flag to true. We consider the length of strs[i] if and only if the flag is false.
*/
class Solution {
public:
    bool helper(string a, string b){
        if(a.compare(b)==0)
            return true;
        int i=0,j=0;
        while(i<a.size() && j<b.size()){
            if(a[i]==b[j++])
                i+=1;
        }
        
        return (i==a.size());
    }
    
    int findLUSlength(vector<string>& strs) {
        int i,j,l=0,ans=-1;
        for(i=0;i<strs.size();i++){
            bool flag=false;
            l=strs[i].length();
            for(j=0;j<strs.size();j++){
                if(i!=j && helper(strs[i],strs[j])==true)
                    flag=true;
            }
            
            if(flag==false)
                ans=max(ans,l);
        }
        
        return ans;
    }
};







/*
class Solution {
public:
    int findLUSlength(vector<string>& strs) {
        int i,j,l=0,t=true,ans=0;
        vector<int> marker(strs.size(),0);
        
        for(i=0;i<strs.size()-1;i++){
            for(j=i+1;j<strs.size();j++){
                if(marker[i]==1 && j==i+1)
                    break;
                if(strs[i]==strs[j]){
                    t=false;
                    marker[i]=1;
                    marker[j]=1;
                }
                else{
                    int a=strs[i].length();
                    int b=strs[j].length();
                    l=max(l,max(a,b));
                }
            }
            if(t==false)
                t=true;
            else
                ans=max(ans,l);
            l=0;
        }
        if(marker[strs.size()-1]!=1){
            int c=strs.back().length();
            ans=max(ans,c);
        }
        
        return ans;
    }
};
*/
