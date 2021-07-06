/*
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
*/





/**
 * @param {string} s
 * @return {string[][]}
 */
function palindrome(s,l,r){						//Checks whether the string within the specified limits are palindrome or not
    while(l<r){
        if(s[l]==s[r]){
            l++;
            r--;
        }else
            return false;
    }
    return true;
}

var partition = function(s) {
    var l=[];
    var ans=[];
    
    function partitions(idx){
        if(idx==s.length){
            ans.push(l.slice());				//*//	//If the index reaches the end, we push a COPY of 'l' into ans. So that when l changes again, it dosen't 
            											//affect the ans.
            return;
        }
        
        for(var i=idx;i<s.length;i++){
            if(palindrome(s,idx,i)){
                l.push(s.substring(idx,i+1));			//We push into l, only when it is a palindrome
                partitions(i+1);
                l.pop();						//*//	//We pop the last entry so that the same l in the current level can be used for future recursions
            }
        }
        return ans;
    }    
    
    return partitions(0);
};





/*
function palindrome(s){
    var l=0
    var r=s.length-1
    while(l<r){
        if(s[l]==s[r]){
            l++;
            r--;
        }else
            return false;
    }
    return true;
}

function partitions(s,l,ans){
    var i;
    if(s.length==0){
        if(l in ans)
            return 0;
        else
            return l;
    }
    
    for(i=1;i<=s.length;i++){
        var l1=s.substring(0,i);
        if(palindrome(l1)==false)
            return 0;
        l.push(l1);

        var s1=s.substring(i);
        if(partitions(s1,l,ans)!=0)
            ans.push(l.slice());
    }
    return ans;
}

var partition = function(s) {
    return partitions(s,[],[]);
};
*/
