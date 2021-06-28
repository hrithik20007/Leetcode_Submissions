'''
In a town, there are n people labelled from 1 to n.  There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:
Input: n = 3, trust = [[1,2],[2,3]]
Output: -1

Example 5:
Input: n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
'''





class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if trust==[]:
            if n==1:
                return 1
            else:
                return -1
        m=0
        l=[i[1] for i in trust]             #numbers which are trusted 
        l2=[i[0] for i in trust]            #numbers who trust
        c=Counter(l)
        for i in c.keys():
            if c[i]>m:
                m=c[i]
                r=i                         #r stores the number which is trusted the most by other numbers

        n1=c[r]                             #number of numbers which trust r
        if n1==n-1 and r not in l2:         #no. of numbers which trust r should be 1 less than n, where the judge himself dosen't trust himself or anybody else
            return r
        else:
            return -1
