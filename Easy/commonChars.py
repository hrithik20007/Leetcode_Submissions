'''
Given an array words of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order.

Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]
'''





class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l=[]
        c=Counter(words[0])                         #Characters and their frequencies in the first word from the array
        for i in range(1,len(words)):               #Comparing the characters and their frequencies of each word (other than the first), with the first
            for j in c.keys():
                if j in words[i]:
                    if c[j]>words[i].count(j):      #If the characters exists in the other words but the frequency is lesser, it is updated to the lower frequency
                        c[j]=words[i].count(j)
                        
                else:
                    c.pop(j)                        #If the characters are not common, they they are popped from the counter object.

        for i in c.keys():                          #Appending the remaining characters in the counter object to a list and returning the list at the end
            for j in range(c[i]):
                l.append(i)
                
        return l
