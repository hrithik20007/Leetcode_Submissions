'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:
    the first row consists of the characters "qwertyuiop",
    the second row consists of the characters "asdfghjkl", and
    the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []
'''



class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l1=list("qwertyuiop")
        l2=list("asdfghjkl")
        l3=list("zxcvbnm")
        a=0
        b=0
        c=0
        l=[]
        
        for i in words:
            for j in i:
                if j.lower() in l1:
                    a+=1
                if j.lower() in l2:
                    b+=1
                if j.lower() in l3:
                    c+=1

            '''
            Logic is that if all the alphabets are present in one line then either a,b or c should increament to the value of its length. If alphabets are 
            present in different lines, then a, b and c will increament separately and to different values, neither reaching the value of word's length.
            '''
            if a==len(i) or b==len(i) or c==len(i):
                l.append(i)

            #For the next iteration, the values of a,b and c should be initialised to 0 again.
            a=0
            b=0
            c=0
        
        return l
