'''
You are given a string s, return the number of segments in the string. 
A segment is defined to be a contiguous sequence of non-space characters.

Example 1:
Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

Example 2:
Input: s = ""
Output: 0
'''



class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1=s.strip()  #For cases like s="     ".
        if s1=="":
            return 0

        else:
            s2=s1.split(" ") 
            s3=list(filter(None,s2))    #filter() helps in removing all the instances of a particular element from the entire list (i.e. the 1st parameter). Here, filter eliminates ''.
            return len(s3)
