'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        
        for i in s:
            #Append any opening parentheses
            if (i=='(' or i=='{' or i=='['):
                stack.append(i)
                
            #If closing parentheses is found at beginning, returns false; otherwise pops a value and checks whether the popped value is the identical opening parentheses.   
            if (i==')' or i=='}' or i==']'):
                if len(stack)==0:
                    return False
                else:
                    v=stack.pop()
                    if(i==')' and v!='('):
                        return False
                    if(i=='}' and v!='{'):
                        return False
                    if(i==']' and v!='['):
                        return False
        
        #If all parentheses were successfully popped, that means the ordering was valid
        if len(stack)==0:
            return True
        '''        
        l=len(s)-1
        f=0
        q=0
        p=0
        for i in s:
            if (i=="("):
                q=q+1
                if(f!=l):
                    if (s[-(f+1)]==")" or s[f+1]==")"):
                        p=p+1

            if (i=="{"):
                q=q+1
                if(f!=l):
                    if (s[-(f+1)]=="}" or s[f+1]=="}"):
                        p=p+1

            if (i=="["):
                q=q+1
                if(f!=l):
                    if (s[-(f+1)]=="]" or s[f+1]=="]"):
                       p=p+1

            f=f+1

        if(p==q and q!=0):
            return True
        else:
            return False
        '''
