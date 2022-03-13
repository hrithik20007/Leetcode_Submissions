/*
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
*/







/*
Logic:
i and j points to the final index of the binary strings. We use a while loop to check whether any of them is 
still left to be completed (while traversing over them from right to left). If yes, we calculate the sum by
adding the current index's element. If it is 2, that means we have to carry 1, while sum can be either 1 or 0,
so we do modulus by 2. We append these sum values to the string and finally return the reversed string.
*/
class Solution {
    public String addBinary(String a, String b) {
        StringBuilder res=new StringBuilder();
        int i=a.length()-1;
        int j=b.length()-1;
        int carry=0,sum=0;
        while(i>=0 || j>=0){
            sum=carry;
            if(i>=0) sum+=a.charAt(i--)-'0';
            if(j>=0) sum+=b.charAt(j--)-'0';
            carry=sum>1?1:0;
            res.append(sum%2);
        }
        
        if(carry!=0) res.append(carry);
        return res.reverse().toString();
    }
}