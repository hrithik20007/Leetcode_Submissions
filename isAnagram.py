#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An anagram of a word is formed by rearranging the alphabets in  that word

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        f=0
        s=list(s)
        t=list(t)
        
        if len(s)==len(t):
            for i in s:
                if i not in t:
                    f+=1
                    break
                else:
                    t.remove(i)  #We remove the elements when matched since otherwise two identical letters in s will give us True even if only a single such letter is present in t.
        else:
            return False
       
        if f==0:
            return True
        else:
            return False
