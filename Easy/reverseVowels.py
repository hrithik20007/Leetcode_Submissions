'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
'''




class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        p2=len(s)-1
        v=set(list("aeiouAEIOU"))
        
        for p1 in range(len(s)):  #Works with 2 pointers. As the starting pointer finds a vowel, the second pointer reduces until it finds another vowel. Then they are reversed.
            if p1>=p2:
                break
            if s[p1] in v:
                while s[p2] not in v:
                    p2-=1
                s[p1],s[p2]=s[p2],s[p1]
                p2-=1
            
        return "".join(s)
        '''
        l=[]
        s1=list(s)
        for i in range(0,len(s1)):
            if (s1[i]=='a' or s1[i]=='e' or s1[i]=='i' or s1[i]=='o' or s1[i]=='u' or s1[i]=='A' or s1[i]=='E' or s1[i]=='I' or s1[i]=='O' or s1[i]=='U'):
                l.append(i)
                
        if l==[] or len(l)==1:
            return s
        else:
            s2=""
            if(len(l)%2==1):
                l1=(len(l)+1)//2-1
                l.remove(l[l1])
                l2=len(l)-1
                l3=0
                for j in range(0,len(s1)):
                    if j==l[l3]:
                        s2=s2+s1[l[l2]]
                        l2-=1
                        l3+=1
                    else:
                        s2=s2+s1[j]
            else:
                l2=len(l)-1
                l3=0
                for j in range(0,len(s1)):
                    if j==l[l3]:
                        s2=s2+s1[l[l2]]
                        l2-=1
                        l3+=1
                    else:
                        s2=s2+s1[j]

            return str(s2)
        '''
