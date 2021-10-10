/*
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
*/




/*
Logic: FIrst we calculate the total length and store m as the number before the middle node. When we traverse
until m, we actually have temp2 pointer as the node pointing to the middle node.
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
    ListNode* middleNode(ListNode* head) {
        int l=0;
        
        ListNode *temp1=head;
        ListNode *temp2=head;
        while(temp1!=NULL){
            l+=1;
            temp1=temp1->next;
        }
        
        int m=floor(l/2);

        while(m!=0){
            temp2=temp2->next;
            m-=1;
        }
        
        return temp2;
    }
};