/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in 
reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a 
linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
*/





/*
Logic: We add the digits of the consecutive nodes from the two lists in the order provided. As they are in
reverse order, we are actually adding the rightmost digits of the actual numbers as we do in real life. We keep
track of the carry and add that with the next nodes' added values. We iterate the lists using a while loop which
stays valid as long as either of the two lists are left to be traversed fully or if the carry is not 0.
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head=new ListNode();               //The first node is a dummy node
        ListNode *temp1=head;
        
        int carry=0;
        while(l1!=NULL || l2!=NULL || carry!=0){
            int a=(l1==NULL)?0:l1->val;
            int b=(l2==NULL)?0:l2->val;

            //Sum of the two numbers from the two nodes
            int sum=a+b+carry;
            int value=sum%10;                       //2nd digit if the sum is in double digits (1st in case of single digits)
            carry=floor(sum/10);                    //1st digit if the sum is in double digits (0 in case of single digits)
            
            ListNode *temp2=new ListNode(value);    //New node with the added value (without the carry)
            temp1->next=temp2;
            temp1=temp2;                            //temp1 pointer is updated to the last node
            
            //Pointers are updated
            l1=(l1==NULL)?NULL:l1->next;            //The pointers are sent forward by one place unless NULL
            l2=(l2==NULL)?NULL:l2->next;
        }
        
        temp1->next=NULL;                           //The last node is pointed to NULL
        return head->next;                          //As head was a dummy node, the actual list starts from the next node
    }
};





/*
    int number(ListNode *temp){
        long long a,ans=0,i=0;
        
        while(temp!=NULL){
            a=pow(10,i);
            ans+=temp->val*a;
            i+=1;
            temp=temp->next;    
        }
        
        return ans;
    }
    
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *temp1=l1;
        ListNode *temp2=l2;
        int n1=number(temp1);
        int n2=number(temp2);
        int f=0;
        
        int add=n1+n2;
        
        ListNode *head=NULL;
        
        if(add==0){
            ListNode *t=new ListNode(add%10);
            head=t;
        }
        
        while(add>0){
            ListNode *t=new ListNode(add%10);
            if(head==NULL)
                head=t;
            else{
                ListNode *tempo=head;
                while(tempo->next!=NULL){
                    tempo=tempo->next;
                }
                tempo->next=t;
            }
            add=add/10;
        }
        
        return head;
    }
};
*/