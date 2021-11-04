/*
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list 
from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
*/





/*
Logic: We use four pointers to mark the left and right nodes as well as the ones before and after it. We reverse the nodes
between the left and right nodes and connect the reversed list to the original using the pointers marking the nodes before
and after it.
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
    ListNode *reverse(ListNode *head, ListNode *tail){
        ListNode *prev=NULL, *curr=head, *nex;
        
        while(prev!=tail){
            nex=curr->next;
            curr->next=prev;
            prev=curr;
            curr=nex;
        }
        
        return prev;
    }
    
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if(head==NULL || head->next==NULL || left==right)
            return head;
        
        ListNode *bh=NULL, *h=NULL, *t=NULL, *at=NULL;
        ListNode *temp=head;
        int l=1;
        
        while(temp!=NULL){
            if(l==left-1)
                bh=temp;
            if(l==left)
                h=temp;
            if(l==right)
                t=temp;
            if(l==right+1)
                at=temp;
            
            temp=temp->next;
            l+=1;
        }
        
        ListNode *newhead=reverse(h,t);
        if(bh!=NULL)
            bh->next=newhead;
        if(at!=NULL)
            h->next=at;
        

        if(left!=1)
            return head;
        else
            return newhead;
    }
};