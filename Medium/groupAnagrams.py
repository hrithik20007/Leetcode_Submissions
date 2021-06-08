'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''




class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            j=''.join(sorted(i))    #Since sorted() will return a list of characters
            if j in d.keys():
                d[j].append(i)
            else:
                d[j]=[i]
                
        ans=[j for i,j in d.items()]    #Appending all dictionary values' lists to ans
        return ans
        

        
        '''
        l1=[]
        l2=[]
        ans=[]
        c=Counter(strs)
        for i in range(len(strs)):
            l1=[]
            if c[strs[i]]>1 and strs[i] not in l2:
                for i1 in range(c[strs[i]]):
                    l1.append(strs[i])
                    l2.append(strs[i])
            if strs[i] not in l2:
                l1.append(strs[i])
                l2.append(strs[i])
            n=permutations(strs[i])
            for j in list(n):
                j1=''.join(j)
                if j1 in strs and j1 not in l2:
                    l1.append(j1)
                    l2.append(j1)
            
            if len(l1)!=0:
                ans.append(l1)
            
        return ans
        '''
