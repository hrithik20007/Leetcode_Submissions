/*
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
*/




/*
Logic: 
We use recursion to reach the last node and then as we go back the recursion steps, we compare the nodes' values
to those from the front using a global linked list pointer called temp.
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
    ListNode *temp=NULL;
    
    bool palin(ListNode *head){
        if(head==NULL)
            return true;
        
        bool ans=palin(head->next);
        if(ans && head->val==temp->val){
            temp=temp->next;
            return true;
        }
        else
            return false;
    }
    
    bool isPalindrome(ListNode* head) {
        temp=head;
        return palin(head);
    }
};