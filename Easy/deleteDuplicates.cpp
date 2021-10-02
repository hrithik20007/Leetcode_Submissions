/*
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return 
the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
*/





/*
Logic: temp is initialiased to the head and is used to traverse the list. If temp's next node is same as temp,
we point temp to its next's next node and the next node is deleted.
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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* temp=head;
        
        while(temp!=NULL && temp->next!=NULL){
            if(temp->val==temp->next->val){
                ListNode* todelete=temp->next;
                temp->next=temp->next->next;
                delete todelete;
            }
            else
                temp=temp->next;
        }
        
        return head;
    }
};