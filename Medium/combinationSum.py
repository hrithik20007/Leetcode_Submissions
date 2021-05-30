'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Example 4:
Input: candidates = [1], target = 1
Output: [[1]]

Example 5:
Input: candidates = [1], target = 2
Output: [[1,1]]
'''




'''
We are going to use backtracking to solve this problem. We have three base cases to consider. Case 1 => We have reached the target sum. So the remainder
is now 0. We add these numbers that summed to the target to our ans set. Case 2 => We went over the target sum. Case 3 => We have considered all the
numbers. Now we make two calls to rec. One call to choose the number we are currently processing to add to our combination sum. And a second call where we 
do not chose the number we are currently processing and we move on to the next number.
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """ 
        def rec(candidates,index,remainder,l):
            if remainder<0:     #Base case 1: if the difference of the added numbers exceed target
                return
            if remainder==0:    #Base case 2: if the difference is 0. That is, the added numbers equal to the target.
                if sorted(l) not in self.sol:
                    self.sol.append(sorted(l))
            if index>=len(candidates):  ##Base case 3: if the index exceeds the list length
                return

            else:
                rec(candidates,index,remainder-candidates[index],l+[candidates[index]])
                rec(candidates,index+1,remainder,l)
        
        self.sol=[]
        '''
        We can use a single instance of a variable or function (by using the 'self' keyword) so that it can be referenced inside a class function as well.
        We may also use a nonlocal variable but for some reason, the syntax is improper in python2. So I opted to go for 'self' instead.
        Note on nonlocal and global:
        -> nonlocal is used alongwith the variable in a function 'B' which is inside another function 'A'. If we want to use a variable in B, which is also used in A,
        then we use nonlocal to avoid creating a local variable in B using the same name, and to use the one in A. So this is used for nested functions.
        -> We use global if there is only one function (and not nested functions). If we want a variable defined outside a function, to be accessed
        inside the function as well, then we use the global keyword alongwith the one defined inside the function.
        '''
        rec(candidates,0,target,[])
        return self.sol
        
        
        '''
        l=[]
        l1=[]
        for i in candidates:
            i1=i
            d=0
            f=0
            l1=[]
            if i==target:
                l.append([i])
            elif i<target:
                l1.append(i)
                while i1<target:
                    d=target-i1
                    if d==i:
                        l1.append(i)
                        i1+=i
                    elif d in candidates:
                        l1.append(d)
                        i1+=d
                    else:
                        l1.append(i)
                        i1+=i
                        
                if sum(l1)==target:
                    l.append(l1)
            elif i>target:
                continue
                
        return l
        '''
