/*
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
*/







/*
Logic: We use binary search. We take l as the first element while h as the last element. We calculate mid and calculate the number of elements present in the matrix
which have a value <= to the mid's value (also known as the rank of the element in the matrix). If the count is <k, then we do l=mid+1, otherwise we do h=mid.
*/
/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(matrix, k) {
    var l=matrix[0][0];
    var h=matrix[matrix.length-1][matrix[0].length-1];
    var mid,c;

    //For counting the elements<=mid
    function count(matrix){								//If the last element in a row is smaller than the mid, that means the rest of them are smaller too. Thus
    													//we add them to the count. If not, then we decrease j until it is and add all the elements before it. 
        var c1=0,i,j;
        for(i=0;i<matrix.length;i++){
            for(j=matrix[0].length-1;j>=0;j--){
                if(matrix[i][j]<=mid){
                    c1+=j+1;
                    break;
                }
            }
        }
        
        return c1;
    }
    
    
    while(l<h){
        mid=Math.trunc((l+h)/2);
        c=count(matrix);
        if(c<k)
            l=mid+1;
        else
            h=mid;
    }
    
    return l;
};





/*
This also works but it is a brute force approach with O(n^2) time complexity.

var kthSmallest = function(matrix, k) {
    var i,j,l=[];
    for(i=0;i<matrix.length;i++){
        for(j=0;j<matrix[0].length;j++){
            l.push(matrix[i][j]);
        }
    }
    
    l.sort((a,b)=>a-b);
    return l[k-1];
};
*/
