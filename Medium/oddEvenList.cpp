/*
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even 
indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
*/





/*
Logic: All the odd-indexed nodes are joined and all the even-indexed nodes are joined. Finally, the last odd-indexed node
is joined to the first even-indexed node. The last even-indexed node is pointed to NULL.
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
    ListNode* oddEvenList(ListNode* head) {
        if(head==NULL || head->next==NULL)
            return head;
        
        ListNode *newhead=head;
        ListNode *head2=head->next;
        ListNode *t2=head->next;
        
        int l=0,i=3;
        ListNode *temp=head;
        while(temp!=NULL){
            l+=1;
            temp=temp->next;
        }

        temp=head->next->next;
        
        while(i<=l){                       //We start traversing from the third node (i is also 3)
            if(i%2==1){
                head->next=temp;
                head=temp;
            }
            else{
                t2->next=temp;
                t2=temp;
            }
            
            i+=1;
            temp=temp->next;    
        }
        
        head->next=head2;
        t2->next=NULL;
        
        return newhead;
    }
};