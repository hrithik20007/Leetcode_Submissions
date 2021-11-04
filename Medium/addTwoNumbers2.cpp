/*
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]
*/






/*
Logic: Same as addTwoNumbers. The only difference is the numbers are not reversed. Thus, we reverse them first and then 
add them. After adding, we get the answer as reversed, so we reverse that as well to get the required linked list.
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
    ListNode *reverse(ListNode* head){
        ListNode *prev=NULL, *curr=head, *nex;
        
        while(curr!=NULL){
            nex=curr->next;
            curr->next=prev;
            prev=curr;
            curr=nex;
        }
            
        return prev;
    }
    
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head1=reverse(l1);
        ListNode *head2=reverse(l2);
        
        ListNode *newhead=new ListNode();
        ListNode *temp=newhead;
        int carry=0;
        
        while(head1!=NULL || head2!=NULL || carry!=0){
            int a=(head1==NULL)?0:head1->val;
            int b=(head2==NULL)?0:head2->val;
            
            int sum=a+b+carry;
            int value=sum%10;
            carry=floor(sum/10);
            
            ListNode *temp2=new ListNode(value);
            temp->next=temp2;
            temp=temp2;
            
            head1=(head1==NULL)?NULL:head1->next;
            head2=(head2==NULL)?NULL:head2->next;
        }
        
        temp->next=NULL;
        return reverse(newhead->next);
    }
};