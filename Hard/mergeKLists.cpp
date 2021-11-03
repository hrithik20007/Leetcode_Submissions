/*
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
*/





/*
Logic: We merge the first two lists. Then the merged list is merged with the next list and so on.
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
    ListNode *merge(ListNode *l1, ListNode *l2){
        if(l1==NULL) return l2;
        if(l2==NULL) return l1;
        
        ListNode *result=NULL;
        if(l1->val < l2->val){
            result=l1;
            result->next=merge(l1->next,l2);
        }
        else{
            result=l2;
            result->next=merge(l1,l2->next);
        }
        
        return result;
    }
    
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int n=lists.size();
        if(n==0) return NULL;
        
        ListNode *head=lists[0];
        for(int i=1;i<n;i++)
            head=merge(head,lists[i]);
        
        return head;
    }
};