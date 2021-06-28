'''
We are given two sentences s1 and s2.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Return a list of all uncommon words. 
You may return the list in any order.

Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
'''



#Logic: A word is uncommon if it occurs only once even when both the strings are combined.
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l=[]
        l1=s1.split()
        l2=s2.split()
        c=Counter(l1+l2)
        for i in c.keys():
            if c[i]==1:
                l.append(i)
                
        return l
        
        
        '''
        This works but I wanted a faster solution
        
        
        l=[]
        l1=s1.split()
        l2=s2.split()
        for i in l1:
            if i not in l2 and l1.count(i)==1:
                l.append(i)
        for i in l2:
            if i not in l1 and l2.count(i)==1:
                l.append(i)
                
        return l
        '''
