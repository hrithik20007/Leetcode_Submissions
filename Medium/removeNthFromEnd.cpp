/*
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
*/





/*
Logic: First we calculate the total length and deduct the given number to get the node number from the starting
position. We travel to that node and point that node's pointer to its next's next node.
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *temp=head;
        int l=0;                            //l stores the total length
        while(temp!=NULL){
            l+=1;
            temp=temp->next;
        }
        
        int s=l-n;
        
        if(s==0){                           //If the first node has to be deleted
            head=head->next;
        }
        else{                               //If any other node has to be deleted
            int l1=1;
            ListNode *temp2=head;
            while(l1!=s){
                l1+=1;
                temp2=temp2->next;
            }
            temp2->next=temp2->next->next;
        }

        return head;
    }
};