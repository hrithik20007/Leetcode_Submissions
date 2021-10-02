/*
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the 
nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]
*/






/*
Logic: Solved recursively. result is a linked list object initialised at each call. At each call, the current 
head of the smaller-data node (from l1 and l2) is declared to result and this result points to the next call's 
result and so on. Finally, if l1 is exhausted first, then l2's head is declared to result, meaning the rest of
l2 is added to result and vice-versa if l2 is exhausted first. This is how we get the merged sorted list.
However it is important to note that the two lists l1 and l2 have to be sorted first.
*/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1==NULL) return l2;
        if(l2==NULL) return l1;
        
        ListNode* result;
        if(l1->val>l2->val){
            result=l2;
            result->next=mergeTwoLists(l1,l2->next);
        }
        else{
            result=l1;
            result->next=mergeTwoLists(l1->next,l2);
        }
        
        return result;
    }
};