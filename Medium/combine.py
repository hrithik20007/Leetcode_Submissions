'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]
'''





class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l=[i for i in range(1,n+1)]
        
        def recursion(l1,l2,l3,k):
            if l2==[] and len(l1)<k:
                return 0
            if len(l1)==k:
                return 1
            for i in range(len(l2)):
                l4=l1+[l2[i]]               #It is better to use different variables while manipulating for loop variables as it becomes messy to change l1 and 
                                            #then revert it back to its original l1 form after calling the function. It is important to note that in python,
                                            #when we assign a value to a variable or a varible to a variable, that value is a reference (pointer) to an object.
                                            #So the two variables will point to the same object, unless we do something explicit to copy them.
                l5=l2[i+1:]                 #Same as above but in case of l2
                n1=recursion(l4,l5,l3,k)
                if n1==1:
                    l3.append(l4)           #l3 stores the results
            return l3
        
        l3=recursion([],l,[],k)
        return l3
