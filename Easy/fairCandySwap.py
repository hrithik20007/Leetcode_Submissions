'''
Alice and Bob have candy bars of different sizes: aliceSizes[i] is the size of the i-th bar of candy that Alice has, and bobSizes[j] is the size of the j-th bar of candy that Bob has.
Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)
Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange.
If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.

Example 1:
Input: aliceSizes = [1,1], bobSizes = [2,2]
Output: [1,2]

Example 2:
Input: aliceSizes = [1,2], bobSizes = [2,3]
Output: [1,2]

Example 3:
Input: aliceSizes = [2], bobSizes = [1,3]
Output: [2,3]

Example 4:
Input: aliceSizes = [1,2,5], bobSizes = [2,4]
Output: [5,4]
'''



'''
Logic:
Suppose we exhange x from aliceSizes and y from bobSizes. Then --
Sa - x + y = Sb + x -y   [where Sa is the sum of elements of aliceSizes and Sb is that of bobSizes]
=> x = (sa - Sb)//2 +y
'''
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff=sum(aliceSizes)-sum(bobSizes)
        for i in set(bobSizes):
            if i+(diff)//2 in aliceSizes:
                return [i+(diff)//2,i]
        
        '''
        Time Limit Exceeded 
        
        
        x=sum(aliceSizes)
        y=sum(bobSizes)
        l=[]
        for i in range(len(aliceSizes)):
            for j in range(len(bobSizes)):
                x-=aliceSizes[i]
                y+=aliceSizes[i]
                y-=bobSizes[j]
                x+=bobSizes[j]
                
                if x==y:
                    l=[aliceSizes[i],bobSizes[j]]
                    return l
                
                x+=aliceSizes[i]
                y-=aliceSizes[i]
                y+=bobSizes[j]
                x-=bobSizes[j]        
        '''
