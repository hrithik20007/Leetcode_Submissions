'''
n an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of 
lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in 
this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅',
where '∅' is defined as the blank character which is less than any other character (More info).
'''





class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if len(words)==1:       #One=word lists are always sorted
            return True
        l=[]
        w1=words[:]
        w1.sort(key=len)
        n=len(w1[-1])           #Stores the length of the largest word
        
        for i in words:
            i=i.ljust(n,'#')    #The right portion of the shorter words are padded with '#' so that all words have length. We do this using ljust() function.
                                #In case of words with the same length, they remain unaffected.
            l.append(i)         #Appends the new padded words (as well as the old words) to a new list 'l'
        
        order='#'+order         #Priority of '#' is highest (i.e. lexicographically lowest)

        for i in range(1,len(l)):   #Each words' characters at the same indexes are compared
            for j in range(n):
                if order.index(l[i][j])<order.index(l[i-1][j]):     #Returns false if not in lexicographical order
                    return False
                if order.index(l[i][j])>order.index(l[i-1][j]):     #Proceeds to the next pair of words, if the characters in the same index are in lexicographical order
                    break
                
        return True
