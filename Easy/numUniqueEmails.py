'''
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
    For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
    For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.
    For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.
Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.

Example 1:
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

Example 2:
Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3
'''





class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s=[]
        for i in emails:
            l=i.split('@')              #l[0] has the local name while l[1] has he domain name

            #For local name
            if '.' in l[0]:
                l1=l[0].split('.')
                l[0]=''.join(l1)        #stores the local name excluding the '.'
            if '+' in l[0]:
                l2=l[0].split('+')      #stores the local name until the '+'
                l[0]=l2[0]
                                        #The domain name remains as it is 
            r='@'.join(l)
            if r not in s:
                s.append(r)
                
        return len(s)
