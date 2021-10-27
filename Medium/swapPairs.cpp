/*
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without 
modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
*/




/*
Logic:
Initiailly,
prev -> The node before the head node (there is no such node, thus NULL)
curr -> The head node
nex -> The node after the head node
Each time reverse() is called, two nodes are swapped, where initially the starting node becomes curr. When the
recursion backtracks, the prev (the last node before the curr node, which is also the second node by the end of each
reverse() function) node from the first two becomes the newhead as reverse() is called from the swapPairs() function.
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
    ListNode* reverse(ListNode* head){
        ListNode* prev=NULL;
        ListNode* curr=head;
        ListNode* nex;
        
        int l=0;
        while(curr!=NULL && l<2){
            nex=curr->next;
            curr->next=prev;
            prev=curr;
            curr=nex;
            l+=1;
        }
        
        if(curr!=NULL)
            head->next=reverse(curr);
        
        return prev;
    }
    
    ListNode* swapPairs(ListNode* head) {
        ListNode *newhead=reverse(head);
        return newhead;
    }
}; 