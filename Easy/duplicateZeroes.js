/*
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.

Example 1:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
*/





/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
var duplicateZeros = function(arr) {
    var i=0;
    while(i<arr.length){
        if(arr[i]==0){
            arr.splice(i+1,0,0);		//splice() --> First parameter indicates index, second indicates the no. of elements to be deleted and the next ones indicate
            							//the items to be added
            arr.pop();					//Deletes the last element
            i+=2;
        }
        else
            i+=1;
    }    
};




/*
This works but I wanted a faster solution


var duplicateZeros = function(arr) {
    var i=0,j;
    while(i<arr.length-1){
    
        if(arr[i]==0){
            for(j=arr.length-1;j>=i+2;j--)
                arr[j]=arr[j-1];
            arr[i+1]=0;
            i+=2;
        }
        else
            i+=1;
    }
    return;
};
*/
