/*
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the 
end of arr1 in ascending order.

Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
*/





/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var relativeSortArray = function(arr1, arr2) {
    var i,j,d={},l=[];
    for(i of arr1){				//Inputs all word frequencies in a dictionary
        if(i in d)
            d[i]+=1;
        else
            d[i]=1;
    }
    
    for(j of arr2){				//Iterates over the elements in arr2 and pushes them to l in the same order, but in the frequency of arr1
        while(d[j]>0){
            l.push(j);
            d[j]-=1;
        }
    }
    
    arr1.sort((a,b)=>a-b);
    for(i of arr1){				//Pushing the remaining elements in ascending order
        while(d[i]>0){
            l.push(i);
            d[i]-=1;
        }
    }
    
    return l;
};
