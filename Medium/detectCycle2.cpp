/*
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following 
the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to 
(0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
*/




/*
Logic: The slow pointer moves by 1 node while fast moves by 2 nodes. If there is a cycle, they will meet at a certain 
point. Now we move the slow pointer to the head and move both the pointers by one node. Then the point where they meet
is the node where the last node is joined. 
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if(head==NULL || head->next==NULL)
            return NULL;
        
        ListNode *slow=head->next;
        ListNode *fast=head->next->next;
        int f=0;
        
        while(slow!=NULL && fast!=NULL && fast->next!=NULL){
            if(slow==fast){
                f=1;
                break;
            }
            
            slow=slow->next;
            fast=fast->next->next;
        }
        
        if(f==0)
            return NULL;
        
        slow=head;

        while(slow!=fast){
            slow=slow->next;
            fast=fast->next;
        }

        return slow;
    }
};