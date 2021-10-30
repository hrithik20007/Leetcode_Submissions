/*
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than
or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
*/





/*
Logic: We create two dummy nodes head1 and head2. head1's next nodes will form a chain of nodes with value less than x 
while head2's will form a chain of nodes with values greater than x. Finally head1 list is joined to head2 list. head2's
last node is pointed to NULL.
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
    ListNode* partition(ListNode* head, int x) {
        if(head==NULL || head->next==NULL) return head;
        
        ListNode *head1= new ListNode();
        ListNode *head2= new ListNode();
        ListNode *t1=head1, *t2=head2;
        
        while(head!=NULL){
            if(head->val < x){
                t1->next=head;
                t1=t1->next;
            }
            else{
                t2->next=head;
                t2=t2->next;
            }
            
            head=head->next;
        }   
        
            t1->next=head2->next;
            t2->next=NULL;
            return head1->next;
        
        
        
        /*
        ListNode *head1=NULL;
        ListNode *head2=NULL;
        ListNode *temp=head;
        int f1=0,f2=0;
        
        while(temp!=NULL){
            if(f1==0 && temp->val < x){
                f1=1;
                head1=temp;
            }
            if(f2==0 && temp->val > x){
                f2=1;
                head2=temp;
            }
            
            temp=temp->next;
        }
        
        temp=head1;

        ListNode *newhead=head1;
        while(temp!=NULL){
            if(temp->val < x){
                newhead->next=temp;
                newhead=temp;
            }
            temp=temp->next;
        } 
        cout<<"2"<<endl;
        temp=head2;
        newhead->next=temp;
        newhead=temp;
        while(temp!=NULL){
            if(temp->val > x){
                newhead->next=temp;
                newhead=temp;
            }
            temp=temp->next;
        }

        newhead->next=NULL;
        return head1;
        */
    }
};