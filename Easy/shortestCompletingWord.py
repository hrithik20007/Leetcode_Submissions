'''
Given a string licensePlate and an array of strings words, find the shortest completing word in words.
A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.
For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".
Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

Example 1:
Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.

Example 2:
Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"
Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.
'''





class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        l=[]
        l1=[]
        s=''.join([i.lower() for i in licensePlate if i.isalpha()]) #Only takes the lower case of alphanumeric characters
        c1=Counter(s)   #Frequency of all the charcters in the updated form of given word
        
        for i in words:
            f=0
            c2=Counter(i)   #Frequency of all the characters in each word from the 'words' list
            for j in list(set(list(s))):
                if j not in i:  #Checking if all the characters in the original word is present in the word from the list
                    break
                if j in i and c2[j]>=c1[j]: #If the alphabet is present, then its frequency should be greater than equal to that in the word and increamenting f if it is
                    f+=1
            if f==len(list(set(list(s)))):  
                f=-1
                
            if f==-1:
                l.append(i)
                
        n=min(len(i) for i in l)    #Minimum length of the word(s) which statisfy all the conditions
        for a in l:
            if len(a)==n:   #As all the words in l are in order as that in words, then the first one to satisfy our length quota will be our answer
                return a


        #=============== OR =======================

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        l=[]
        l1=[]
        f=0
        s=''.join([i.lower() for i in licensePlate if not i.isdigit() if not ord(i)==32]) #We can consecutively put two if statements like this without using 'and'
        c1=Counter(s)
        
        for i in words:
            f=0
            c2=Counter(i)
            for k in list(set(list(s))):
                if k not in i:
                    f+=1
                    break
            if f==0:
                for j in list(set(list(i))):
                    if j in s and c2[j]>=c1[j]:
                        f+=1
                if f==len(list(set(list(s)))):
                    f=-1
            if f==-1:
                l.append(i)
                
        l.sort(key=len) #Sorting the array as per the length of the string elements
        l1.append(l[0])
        for a in l:
            if len(a)!=len(l[0]):
                l1=l[:l.index(a)]
                break
        for b in words:
            if b in l1:
                return b
