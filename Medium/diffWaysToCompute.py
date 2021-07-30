'''
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. 
You may return the answer in any order.

Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
'''







'''
Logic: We start a loop and when we encounter an operator, we divide the string into two and solve them recursively.
'''
def comp(s):
    operators = ['+', '-', '*']
    res = []
    for i in range(len(s)):
        if s[i] in operators:
            op = s[i]
            left = s[:i]
            right = s[i+1:]
            left_res = comp(left)
            right_res = comp(right)
            for x in left_res:
                for y in right_res:
                    if op == '+':
                        res.append(x+y)
                    elif op == '-':
                        res.append(x-y)
                    elif op == '*':
                        res.append(x*y)
    if len(res) == 0:
        res.append(int(s))
    return res



class Solution(object):
    def diffWaysToCompute(self, expression):
        r = comp(expression)
        return r





'''
class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        operators = ['+', '-', '*']
        res = []
        for i in range(len(s)):
            if s[i] in operators:
                left_res = self.diffWaysToCompute(s[:i])
                right_res = self.diffWaysToCompute(s[i+1])
                for x in left_res:
                    for y in right_res:
                        if s[i] == '+':
                            res.append(x+y)
                        elif s[i] == '-':
                            res.append(x-y)
                        elif s[i] == '*':
                            res.append(x*y)
        if len(res) == 0:
            res.append(int(s))
        return res
'''
