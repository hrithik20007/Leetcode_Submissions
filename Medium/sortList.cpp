/*
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
*/






/*
Logic: We take all the node values in a vector. Sort that vector. Then re-initialise the node values as the sorted vector
values.
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
    ListNode* sortList(ListNode* head) {
        vector<int> v;
        ListNode *temp=head;
        
        while(temp!=NULL){
            v.push_back(temp->val);
            temp=temp->next;
        }
        
        sort(v.begin(),v.end());
        
        temp=head;
        int i=0;
        while(temp!=NULL){
            temp->val=v[i];
            i+=1;
            temp=temp->next;
        }
        
        return head;
    }
};