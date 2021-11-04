/*
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of 
being chosen.
Implement the Solution class:
Solution(ListNode head) Initializes the object with the integer array nums.
int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally 
likely to be choosen.

Example 1:
Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
*/






/*
Logic: A linked list is initialised. We generate a random value by rand() (which generates a random value in [0,RAND_MAX),
which is 32767). We ensure this random value is in [0,l), l being the length of the linked list, by doing modulus(%) with
l. Then we traverse to the (random+1)th node and return its value. 

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
    ListNode *h;
public:
    Solution(ListNode* head) {
        h=head;
    }
    
    int getRandom() {
        ListNode *temp=h;
        int l=0;
        while(temp!=NULL){
            l+=1;
            temp=temp->next;
        }
        
        int r=rand()%l;
        temp=h;
        for(int i=0;i<r;i++){
            temp=temp->next;
        }
        
        return temp->val;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */