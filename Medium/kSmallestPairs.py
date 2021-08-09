'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
'''







'''
Logic: Heap in python is a MinHeap binary tree and its first element is sure to be the smallest number (takes into acccount the first element if a list). That number
is also the one which is popped when we do heappop(). We store each element in heap as the sum of the elements at index i from num1 and index j from num2, index i 
and index j. We pop the element with the smallest sum while iterating the range of k and store them as the new i and j. Then we add i+1,j and i,j+1 elements to the 
heap. Take note that when we pop during the beginning of the while loop, one remains from the previous iteration - either i+1,j or j+1,i. Thus no element is getting
skipped. We utilise that during the next iteration for the minimum. We also add the indexes we have added to the heap, to a set so as to avoid duplicates.
'''
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        N = len(nums1)
        M = len(nums2)
        
        h = [[nums1[0] + nums2[0], 0, 0]]
        visited = set([(0, 0)])
        res = []
        
        while k > 0 and h:
            s, i, j = heapq.heappop(h)
            res.append([nums1[i], nums2[j]])
            
            if i + 1 < N and (i + 1, j) not in visited:
                heapq.heappush(h, [nums1[i+1] + nums2[j], i + 1, j])
                visited.add((i + 1, j))
            
            if j + 1 < M and (i, j + 1) not in visited:
                heapq.heappush(h, [nums1[i] + nums2[j+1], i, j + 1])
                visited.add((i, j + 1))
            
            k -= 1
        
        return res
        
        
        
        
        '''
        res = []
        arr = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(arr,(-1*(i+j),(i,j)))
            
                if len(arr)>k:
                    heapq.heappop(arr)

        while len(arr)>0:
            res.insert(0,(heapq.heappop(arr))[1])
            
        return res
        '''
