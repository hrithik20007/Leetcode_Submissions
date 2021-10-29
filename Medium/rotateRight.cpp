/*
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
*/




/*
Logic: At first, we count the number of nodes as l. We deduct k from l to get r (k=k%l for cases where k>l). Then we move
our temp2 pointer to the r-th node from the beginning (which is the k-th node from the end). Also the t pointer points to
the last node. Finally, the last node is pointed to the first node. The node next to the temp2-pointed node becomes the 
new head. The temp2-pointed node is pointed to NULL (meaning it becomes the last node).
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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==NULL)
            return head;
        
        ListNode *temp=head;
        ListNode *t=NULL;
        
        int r,l=0;
        while(temp!=NULL){
            l+=1;
            if(temp->next==NULL)
                t=temp;
            temp=temp->next;
        }
        
        k=k%l;
        r=l-k;
        
        ListNode *temp2=head;
        int l1=1;
        while(l1!=r && temp2!=NULL){
            l1+=1;
            temp2=temp2->next;
        }
        
        t->next=head;
        head=temp2->next;
        temp2->next=NULL;
        
        return head;
    }
};