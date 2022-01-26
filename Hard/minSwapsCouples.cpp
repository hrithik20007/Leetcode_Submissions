/*
There are n couples sitting in 2n seats arranged in a row and want to hold hands.
The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat. 
The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last 
couple being (2n - 2, 2n - 1).
Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two 
people, then they stand up and switch seats.

Example 1:
Input: row = [0,2,1,3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

Example 2:
Input: row = [3,2,0,1]
Output: 0
Explanation: All couples are already seated side by side.
*/







/*
Logic:
Observation is that beside an odd element, the number 1 less than it is its partner while for even elements, its partner is
1 more than itself. We use XOR to take care of that. We only change the elements at the odd indexes in case of a mismatch.
It doesn't matter though, as we have to change either the first or second partner in case of a mismatch (dosen't matter 
which). We use a map to keep track of all the elements' indexes. If we find a mismatch, we swap the element at the (i+1)th
position with the correct element.
*/

class Solution {
public:
    int minSwapsCouples(vector<int>& row) {
        int n=row.size();
        map<int,int> mp;
        
        int i,first,second;
        for(i=0;i<n;i++)
            mp[row[i]]=i;
        
        int c=0;
        for(i=0;i<n;i+=2){
            first=row[i];
            second=first^1;                 //What the next element should be after the i-th element
            
            if(mp[second]!=i+1){
                c+=1;
                int temp1=row[i+1];         //Element at (i+1)th index
                int temp2=second;           //Element that should be next to i-th eleement
                int temp3=mp[second];       //Index of temp2
                row[i+1]=temp2;
                row[temp3]=temp1;
                mp[temp1]=temp3;
                mp[temp2]=i+1;
            }
        }
        
        return c;
    }
};