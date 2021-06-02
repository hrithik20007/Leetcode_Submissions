'''
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.
If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Example 1:
Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
'''





lass Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()                #Sorts lexicographically
        d={}
        s=""
        for i in words:
            if len(i)==1 or i[:len(i)-1] in d:  
                if len(i)>len(s):   #If i is 'm' and previously it was 'e', then s will store 'e' as their lengths are equal.
                                    #This helps in maintaining the lexicographical sequence.
                    s=i
                d[i]=1              #All single alphabets and multi-letter words(only whose substrings are already present in the dictionary)
                                    #are added to the dictionary.
        return s



        
        '''
        words.sort(key=len)
        l1=[]
        l2=[]
        f=0
        for i in range(len(words)-1,-1,-1):
            if len(words[i])==1:
                break
            c=0
            for j in  range(len(words[i])-1,0,-1):
                if words[i][0:j] not in words:
                    break
                if words[i][0:j] in l1:
                    f=1
                    if words[i] not in l1:
                        l2.append(words[i])
                    break
                if words[i][0:j] in words and words[i][0:j] not in l1:
                    c+=1
                    l1.append(words[i][0:j])
            if f==1:
                break
            if c==len(words[i])-1:
                l2.append(words[i])
            else:
                if len(l2)==0:
                    l1=[]

        if len(l2)!=0:
            l2.sort()
            return(l2[0])
        else:
            return words[0]
        '''
