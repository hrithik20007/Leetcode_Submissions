'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.

Example 1:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''




class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        '''
        This is my solution and it works but I wanted a faster solution.
        Logic of this solution is that if the frequency of any character in ransomNote is more than that in magazine, it means that all the words in magazine 
        cannot form ransomNote and thus, the output becomes False. Counter() gives a set within a list containing the characters as keys and their frequencies 
        as values.
        
        c1=collections.Counter(ransomNote)
        c2=collections.Counter(magazine)
        f=0
        for i in ransomNote:
            if c1[i]>c2[i]:
                f+=1
                break

        if f!=0:
            return False
        else:
            return True
        '''
        
        result=True
        for i in ransomNote:
            if i in magazine:
                magazine=magazine.replace(i,'',1)  #3rd parameter tells the replace function the first n characters which are to be replaced. Here n=1. (i.e. only the first occurence is replaced)
            else:
                result=False
        return result
