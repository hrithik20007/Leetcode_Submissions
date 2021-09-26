/*
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) 
parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
*/







/*
Logic: Watch video of Anish to get the concept.
*/
class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> st;
        st.push(-1);
        int l=0;
        
        for(int i=0;i<s.length();i++){
            if(s[i]=='(')
                st.push(i);
            else{
                if(!st.empty())
                    st.pop();
                if(!st.empty())
                    l=max(l,i-st.top());
                else
                    st.push(i);                 //The valid parentheses will occur after this index
            }
        }
        
        return l;
    }
};