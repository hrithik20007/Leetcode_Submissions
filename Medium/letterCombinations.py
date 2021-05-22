'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]


ALL 3 SOLUTIONS WORK WITH ALMOST THE SAME SPEEDS (AROUND 94%). I PREFER THE FIRST OPTION.
'''




'''
Logic example:
For "23", steps --
["a","b","c"]->
["b","c","ad","ae","af"]->
["c","ad","ae","af","bd","be","bf"]
["ad","ae","af","bd","be","bf","cd","ce"."cf"]
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0:
            return []
        d={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        r=[""]
        for i in digits:
            for j in range(len(r)):
                s=r.pop(0)
                for k in d[i]:
                    r.append(s+k)

        return r
    
    


        '''
        if len(digits)==0:
            return []
        d={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}

        s=map(d.get,digits)     #map performs a function (1st parameter) on the items in the iterable (2nd parameter) and gives a map object which we convert to list

        s=itertools.product(*s)     #This function gives us al the possible combinations(as tuples) of the provided lists in the parameter (*s gives us the lists within the map object s) -->  Eg: For [1,2] and [3,4], we get [(1,3),(1,4),(2,3),(2,4)] 

        s=map(''.join,s)    #The products we get in the previous line are tuples. By this line, we convert each tuple into a string made by joining the tuple elements

        return list(s)
        '''
    


        '''
        l=[]
        l1=[]
        d={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        for i in digits:
            l.append(d[i])
        
        if len(digits)==1:
            return d[digits[0]]
        elif len(digits)==2:
            for i in l[0]:
                for j in l[1]:
                    l1.append(i+j)
            return l1
        elif len(digits)==3:
            for i in l[0]:
                for j in l[1]:
                    for k in l[2]:
                        l1.append(i+j+k)
            return l1
        elif len(digits)==4:
            for i in l[0]:
                for j in l[1]:
                    for k in l[2]:
                        for m in l[3]:
                            l1.append(i+j+k+m)
            return l1
        '''
