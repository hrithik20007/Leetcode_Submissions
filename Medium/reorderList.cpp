/*
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
*/




/*
Logic: We use two pointers, one to traverse from the beginning and one from the end. Then we change the links in such a 
way that the node at front is connected to the one at the back and the node at the back is connected to the next node
after the front node (The front and back node is indicated by the pointers at the beginning and the end respectively).
The mid-node is found by using slow and faster pointers. fast pointer moves by two nodes while slow node moves by one 
node. When the fast pointer reaches NULL or the last node, the slow pointer will indicate the mid-node. Now, we reverse 
all the links after the mid-node. We do this, to enable the last pointer to move from the back towards the front.
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
    void reorderList(ListNode* head) {
        if(head==NULL || head->next==NULL || head->next->next==NULL)
            return;
        
        //Finding the mid-node, starting from which all the links are reversed
        ListNode *slow=head;
        ListNode *fast=head;
        while(fast && fast->next){
            fast=fast->next->next;
            slow=slow->next;
        }
        
        ListNode *second=slow;      //The mid-node

        //All the links are reversed, starting from mid-node
        ListNode *prev=NULL, *curr=second, *nex=curr->next;
        while(curr!=NULL){
            curr->next=prev;
            
            prev=curr;
            curr=nex;
            if(curr!=NULL)
                nex=curr->next;
        }
        
        ListNode *head2=prev;
        
        ListNode *temp=head;
        ListNode *newhead=head;
        ListNode *t1=head->next;
        ListNode *t2=head2->next;

        //The two pointers are used to change the links interconnecting the first and last nodes alternatingly
        while(head!=head2){
            head->next=head2;
            head2->next=t1;
            head=t1;
            head2=t2;
            if(head->next==head2 || head==head2)
                break;
            t1=t1->next;
            t2=t2->next;
        }

        //The last node is pointed to NULL      
        head2->next=NULL;
        return;
    }
};