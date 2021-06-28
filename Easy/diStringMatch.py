'''
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
    s[i] == 'I' if perm[i] < perm[i + 1], and
    s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

Example 1:
Input: s = "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: s = "III"
Output: [0,1,2,3]

Example 3:
Input: s = "DDI"
Output: [3,2,0,1]
'''



'''
Logic: When we are putting bigger and smaller numbers, we would likely prefer to exhaust our most extreme (biggest and smallest) numbers first, otherwise 
we may have a conflict for a smaller or larger number at a later stage. We have used a two-pointer approach which, at the beginning, are at the extremes and then
move towards each other until they converge.
'''
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        p=[i for i in range(len(s)+1)]              #Represents the array perm. This is sorted.
        perm=[]                                     #Stores the required permutation of perm.
        l=0                                         #Starting pointer
        r=len(p)-1                                  #Ending pointer
        
        for i in s:
            if i=='I':
                perm.append(p[l])
                l+=1
            else:
                perm.append(p[r])
                r-=1
                
        perm.append(p[r])                          #At the end, one digit is remaining to be appended. r and l are at the same place, so we can append the digit
                                                   #at either l or r's index
        return perm
