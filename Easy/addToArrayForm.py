'''
The array-form of an integer num is an array representing its digits in left to right order.
    For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

Example 1:
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:
Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

Example 4:
Input: num = [9,9,9,9,9,9,9,9,9,9], k = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000
'''




class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n=int(''.join(map(str,num)))              #map() turns the list into a list of strings. We join them after that using join() and convert that into an integer.
                                                  #In map() function, we pass a function as the first parameter which is done upon an iterable, which is the second
                                                  #parameter.
        n+=k
        return list(str(n))
