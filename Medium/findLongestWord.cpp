/*
Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If 
there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"

Example 2:
Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"
*/






/*
Logic: At first we sorted the dictionary vector by the strings' length and lexicographical order (longest length and smallest lexical order at first) by using our
own sort comparator (We return true when we need to put a before b).  After that, we start two pointers from 0, for each of the strings s and dictionary[i]. 
If all the letters of dictionary[i] match s's (not all of s's but in that order), then the first word to have done so is our required string. 
*/
class Solution {
public:
    string findLongestWord(string s, vector<string>& dictionary) {
        sort(dictionary.begin(), dictionary.end(), [](string&a,string&b){
            if(a.length()>b.length()) return true;
            else if(a.length()==b.length()) return a<b;
            else return false;});
        
        int i;
        for(i=0;i<dictionary.size();i++){
            if(dictionary[i].length()>s.length())
                continue;
            
            int j=0,k=0;
            while(j<dictionary[i].length() && k<s.length() && (s.length()-k)>=(dictionary[i].length()-j)){  //The letters remaining to be checked should be more for s
                if(dictionary[i][j]==s[k++])
                    j+=1;
            }
            if(j==dictionary[i].length()) return dictionary[i];												//Meaning all letters of dictionary[i] are in s in that order
        }
    
        return "";
    }
};
