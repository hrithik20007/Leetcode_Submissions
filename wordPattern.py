'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
'''



class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s1=list(pattern)
        s2=s.split(" ")
        
        if len(s1)!=len(s2): 
            return False
        else:
            d={}
            c=[]
            
            f=0  #Flag value
            
            for i in range(len(s1)):  #Inserting key value pairs in a dictionary and checking if the value matches a key in case it is repeated.
                if s1[i] not in d:
                    d[s1[i]]=s2[i]
                else:
                    if d[s1[i]]!=s2[i]:
                        f+=1
                        break

            j=0
            for key,value in d.items():  #Different keys may have same values which is not allowed. So we are checking for uniqueness and increase f if its not.
                if value not in c:
                    c.append(value)
                else:
                    f+=1
                    break
                j+=1

            if f==0:
                return True
            else:
                return False


#------------------------------------------------------------------------------------------------------------------------------------------------

        '''
        OR (This works better but isn't my own)


        
        s1=list(pattern)
        s2=s.split(" ")
        if len(s1)!=len(s2):
            return False
        else:
            for i in range(len(s1)):
                if s1.index(s1[i])!=s2.index(s2[i]):  #Works on the logic that the words which follow the pattern will have new words/alphabets at the same index.
                    return False
            return True
        '''

#------------------------------------------------------------------------------------------------------------------------------------------------

        '''
        OR (Another way of doing it)

        #zip() maps the keys of unique elements of one list/string with their corresponding elements the same index from another list/string. They generate
        unique key-value pairs.
        It returns an iterator object and can be displayed using set(). set() is used to represent a set of UNIQUE elements within {} (however, not dictionary).
        Eg of a zipped object: {('a', 'dog'), ('b', 'dog')} from ['a','b','b','a'] and ['dog','dog','dog','dog']. (This is displayed using set().
                             & {('a', 'dog'), ('a', 'cat'), ('b', 'dog'), ('b', 'cat')} from ['a','b','b','a'] and ['dog','dog','cat','cat'].                              
        Eg of a set: {'a','b','c'}


        s1=list(pattern)
        s2=s.split(" ")
        return (len(set(zip(s1,s2))))==len(set(s1))==len(set(s2)) and len(s1)==len(s2)
        '''
