/*
Given a string array words, return the maximum value of length(word[i])*length(word[j]) where the two words do not share common letters. If no such two words 
exist, return 0.

Example 1:
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

Example 2:
Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".

Example 3:
Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
*/





/*
Logic: We convert the characters into their numeric values starting from 0 for 'a'. Then we use them as setBit positions and construct an integer for a complete word.
Thus when we 'AND' these two integers, we get 0 only for those words where there is no common characters. After putting that conditon, we calculate the maximum 
product of the lengths of such words.
*/
/**
 * @param {string[]} words
 * @return {number}
 */
var maxProduct = function(words) {
    var int_bits=[],max=0,i,j,k;
    for(i=0;i<words.length;i++){
        var k=0;
        for(j=0;j<words[i].length;j++){
            k|=(1<<(words[i].charCodeAt(j)-97));						//k will store the bit equivalent of the given word
        }
        int_bits.push(k);												//All such 26-group-bits are added to the list int_bits  
    }

    for(i=0;i<words.length-1;i++){
        for(j=i+1;j<words.length;j++){
            if(!(int_bits[i]&int_bits[j]))								//Only if the 'AND' operation gives 0
                max=Math.max(max,(words[i].length*words[j].length));	//Max product is calculated
        }
    }
    
    return max;
};




/*
This works but I wanted a faster solution




var maxProduct = function(words) {
    var i,j,k1,k2,f=0,max=Number.MIN_SAFE_INTEGER;
    for(i=0;i<words.length-1;i++){
        for(j=i+1;j<words.length;j++){
            var d={};
            var s=words[i].length*words[j].length;
            
            for(k1=0;k1<words[i].length;k1++){
                if(words[i][k1] in d)
                    d[words[i][k1]]+=1;
                else
                    d[words[i][k1]]=1;
            }
            
            for(k2=0;k2<words[j].length;k2++){
                if(words[j][k2] in d){
                    f=1;        
                    break;
                }
            }
            
            if(f==1)
                f=0;
            else
                max=Math.max(max,s);
        }
    }
    
    if(max==Number.MIN_SAFE_INTEGER)
        return 0;
    else
        return max;
};
*/
