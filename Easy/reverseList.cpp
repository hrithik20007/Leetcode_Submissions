/* 
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
*/




/*
Solved via recursion. When the recursion function reaches the last node, it returns that node as 'newhead'.
All the previous nodes are pointed to their previous nodes. Finally the original head is pointed to NULL.
We use 'newhead' as the new pointer to the head of the list.
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
    ListNode* reverse(ListNode *head){
        if(head==NULL || head->next==NULL)
            return head;
        
        ListNode *newhead=reverse(head->next);
        head->next->next=head;
        return newhead;
    }
    
    ListNode* reverseList(ListNode* head) {
        ListNode *newhead=reverse(head);
        if(head!=NULL)
            head->next=NULL;
        return newhead;
    }
};