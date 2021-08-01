/*
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper and citations is sorted in an ascending 
order, return compute the researcher's h-index.
According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers 
have no more than h citations each.
If there are several possible values for h, the maximum one is taken as the h-index.
You must write an algorithm that runs in logarithmic time.

Example 1:
Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:
Input: citations = [1,2,100]
Output: 2
*/






/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    var length=citations.length;		//Think of length as the number of research papers from the end of the array
    var l=0;
    var h=citations.length-1;
    
    if(length==1){						//If there is only one element in citations
        if(citations[0]>=1)
            return 1;
        else
            return 0;
    }
    else if(length<=citations[0])		//If the lowest no. of citations is more than or equal to the number of papers published 
        return length
    else if(1>=citations[length-1]){
        if(1>citations[length-1])		//If the most number of citations is still 0
            return 0;
        else 
            return 1;					//If the most number of citations is 1
    }
    
    
    while(l<=h){						//Basically we are trying to find the first c<=citations[i], where c=length-i (Imagine it as the no. of papers from the end 
    									//of array)
    	var mid=Math.trunc((l+h)/2);
        
        if(l==h)
            return length-mid;
        if((length-mid)==citations[mid])
            return length-mid;
        if((length-mid)>citations[mid])
            l=mid+1;
        if((length-mid)<citations[mid])
            h=mid;
    }
};
