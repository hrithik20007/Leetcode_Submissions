'''
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.
Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:

Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"
'''




class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        #Fact: We can also directly compare character orders. That is, if we check 'a'<'b', it will return True
        
        n=ord(target)   #ord() gives the ascii value of a provided character
        j=n
        while True:
            j+=1
            if j==123:
                j=97
            if chr(j) in letters:
                r=chr(j)
                break
        
        return r
