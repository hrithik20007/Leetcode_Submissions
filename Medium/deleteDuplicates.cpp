/*
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from 
the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
*/





/*
Logic: There are three pointers. If the current pointer and the nex pointer have the same value, the nex pointer is 
increased to the node where there is no longer a match. Then the prev pointer's next is pointed to the nex pointer, 
meaning the curr pointer's node and all its repititions have been skipped.
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
         if(head==NULL)
            return head;
        
        ListNode *prev=NULL, *curr=head, *nex=head->next;
        while(nex!=NULL){
            if(curr->val==nex->val){
                while(nex!=NULL && curr->val==nex->val)
                    nex=nex->next;
                if(prev==NULL)
                    head=nex;
                else
                    prev->next=nex;
            }
            
            else
                prev=curr;
            
            curr=nex;
            if(curr!=NULL)
                nex=curr->next;
        }

        return head;
    
    /*
        ListNode *temp=head;
        
        while(temp!=NULL){
            if(temp->next!=NULL && temp->next->val==temp->val)
                temp->next=temp->next->next;
            else
                temp=temp->next;
        }
        
        return head;
    */
    }
};