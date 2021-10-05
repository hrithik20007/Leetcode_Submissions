/*
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has 
Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
*/





/*
Logic: First we check if the starting node has the value. If it does, we move the head by one node and delete
the original head. Then we simply traverse and check if the next node has the value. If it does, we move the 
current node's pointer to next node's next node.
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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *temp= head;
        
        while(temp!=NULL && temp->val==val){
            ListNode *todel=temp;
            temp=temp->next;
            head=temp;
            delete todel;
        }
        

        while(temp!=NULL && temp->next!=NULL){
            if(temp->next->val==val){
                temp->next=temp->next->next;
            }
            else
                temp=temp->next;
        }
        
        return head;
    }
};