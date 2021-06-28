'''
We define the usage of capitals in a word to be right when one of the following cases holds:
    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.
'''



class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        f=0
        if word.isupper():
            return True
        elif word[0].isupper():
            for i in word[1:len(word)]:
                if i.isupper():
                    f+=1
            if f==0:
                return True
            else:
                return False
        else:
            for i in word[0:len(word)]:
                if i.isupper():
                    f+=1
            if f==0:
                return True
            else:
                return False
