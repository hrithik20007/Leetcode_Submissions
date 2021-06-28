'''
In a string s of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".
A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].
A group is considered large if it has 3 or more characters.
Return the intervals of every large group sorted in increasing order by start index.

Example 1:
Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.

Example 2:
Input: s = "abc"
Output: []
Explanation: We have groups "a", "b", and "c", none of which are large groups.

Example 3:
Input: s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
Explanation: The large groups are "ddd", "eeee", and "bbb".

Example 4:
Input: s = "aba"
Output: []
'''




class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        r=[]
        j=0
        for k,g in groupby(s):      #g will store an object containing the same elements. Like for first example, [a],[b,b],[x,x,x,x] and so on. This
                                    #object can be converted to lists. k will store a computing key for each such object. Here, like [a],[b],[x] and so on.
                                    #A new group object is created everytime the value of k changes.
            gl=len(list(g))
            if gl>=3:
                start=j
                r.append([start,start+gl-1])
            j+=gl
            
        return r


        
        '''
        This works but I wanted a faster solution
        
        
        l=[]
        j=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                j+=1
            if s[i]!=s[i-1]:
                if j>=3:
                    l.append([i-j,i-1])
                j=1
            if i==len(s)-1:
                if j>=3:
                    l.append([i-j+1,i])
                
        return l
        '''
