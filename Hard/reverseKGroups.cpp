/*
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a 
multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example 3:
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example 4:
Input: head = [1], k = 1
Output: [1]
*/






/*
Logic: Reversing k nodes at a time. After reversing each k nodes, the head will point to the first node and the prev will
point to the last node (So actually the prev becomes the new head and the head becomes the last node). The curr pointer
points to the node after the k-th node after each reversal. We aslo put a check whether there are k nodes to be reversed,
otherwise we return.
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
    ListNode *reverse(ListNode* head, int l, int k){
        if(l-k<0)
            return head;
        
        ListNode *prev=NULL, *curr=head, *nex;
        
        int l1=0;
        while(curr!=NULL && l1<k){
            nex=curr->next;
            curr->next=prev;
            prev=curr;
            curr=nex;
            l1+=1;
        }
        
        if(curr!=NULL)
            head->next=reverse(curr,l-k,k);
        
        return prev;
    }
    
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *temp=head;
        int r,j,l=0;
        while(temp!=NULL){
            l+=1;
            temp=temp->next;
        }
        
        ListNode *newhead=reverse(head,l,k);
        return newhead;
    }
};