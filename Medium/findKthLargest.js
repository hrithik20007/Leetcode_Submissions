/*
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
*/




/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    var heap= new MinPriorityQueue();			//An empty heap is created (or initialized)
    
    for(i of nums){
        heap.enqueue(i);						//Pushes elements to the heap (The heap automatically sorts it in ascending order while pushing)
        if(heap.size()>k)
            heap.dequeue();						//Pops the smallest element when the heap's size>k. Thus, by the end, we get k largest elements in the heap. 
    }
    
    return heap.dequeue().element;				//We return the smallest element in the heap, which is actually the kth largest element in nums
};



/*
This works but I wanted a different approach

var findKthLargest = function(nums, k) {
    nums.sort((a,b)=>b-a);
    return nums[k-1];
};
*/
