'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"
'''





class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s)<k:
            return s[::-1]
        else:
            s1=list(s)
            for i in range(0,len(s)+1,2*k):
                #We can assign new values to a place in list which is already filled before. We cannot do this in case of strings.
                #Also, if the full range of the list as per the given limits does not exist, then it will still assign values to the range that does. 
                #However, that does not happen for a single place, where we will be given list index error. 
                s1[i:i+k]=s1[i:i+k][::-1]
                
                
            s2=''.join(s1)
        return s2
        '''
        if len(s)<2*k and len(s)>k:
            r=s[:k][::-1]+s[k:len(s)]
            return r
        else:
            r=""
            i=1
            k2=k
            k1=0
            while(k2<=len(s)):
                if(i%2==1):
                    r+=s[k1:k2][::-1]
                else:
                    r+=s[k1:k2]
                k1+=k
                k2+=k
                i+=1

            if k2>len(s):
                k2-=k
                r+=s[k2:len(s)+1][::-1]

            return r
        '''
