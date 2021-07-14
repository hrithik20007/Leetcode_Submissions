/*
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino 
can be rotated to be equal to another domino.
Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Example 1:
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
*/





/**
 * @param {number[][]} dominoes
 * @return {number}
 */
var numEquivDominoPairs = function(dominoes) {
    var s=0,i,d={};

    for(i of dominoes){					//Sorting each pair and keeping track of their frequencies as d
        i.sort((a,b)=>a-b);
        if(i in d)
            d[i]+=1;
        else
            d[i]=1;
    }

    for(i in d){
        if(d[i]>1){
            s+=((d[i]-1)*d[i])/2;		//The no. of pairs made by n equivalents is equal to the arithmetic sum of 1..to n-1. We thus use ((n-1)*(n))/2
        }
    }

    return s;							//We return the required no. of pairs
};
