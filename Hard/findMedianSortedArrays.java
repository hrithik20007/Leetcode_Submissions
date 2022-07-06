/*
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
*/




/*
Logic: Watch Neetcode's video on it.
*/

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int total,half,l1=nums1.length,l2=nums2.length;
        int a[],b[],am,bm;
        int Ar,Al,Bl,Br;
        
        if(l1<=l2){
            a=nums1;
            b=nums2;
        }
        else{
            a=nums2;
            b=nums1;
        }
        
        total=l1+l2;
        half=(int)total/2;
        
        if(l1==0){
            if(total%2==0) return (float)(nums2[total/2-1]+nums2[total/2])/2;
            else return (float)(nums2[total/2]);
        }
        if(l2==0){
            if(total%2==0) return (float)(nums1[total/2-1]+nums1[total/2])/2;
            else return (float)(nums1[total/2]);
        }
        
        int l=0,r=a.length-1;
        while(true){
            am=(int)(l+r)/2;
            bm=(half-am)-2;
            
            if(am+1>=a.length) Ar=Integer.MAX_VALUE;            //These extreme values are assigned to faciliate 
            else Ar=a[am+1];                                    //picking the other value during max and min
            
            if(am<0) Al=Integer.MIN_VALUE;
            else Al=a[am];
            
            if(bm+1>=b.length) Br=Integer.MAX_VALUE;
            else Br=b[bm+1];
            
            if(bm<0) Bl=Integer.MIN_VALUE;
            else Bl=b[bm];
            
            if(Al<=Br && Bl<=Ar)
                if(total%2==1) return (float)Math.min(Ar,Br);
                else return (float)(Math.max(Al,Bl)+Math.min(Ar,Br))/2;
            else if(Al>Br) r-=1;
            else if(Bl>Ar) l+=1;
        }
    }
}