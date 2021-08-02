/*
Additive number is a string whose digits can form additive sequence.
A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the 
preceding two.
Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:
Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:
Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
*/





/*
Logic: If we look carefully, we will see that whether our string is additive or not is determined by the first two numbers as they will dictate how the additions
will take place afterwards. We use a nested loop to try different combinations of first two numbers and then we use recursion to find out whether these two numbers
will eventually give us an additive string or not. We check this for all possible first two numbers. If none of the combinations work, we return false; otherwise
true.
*/
/**
 * @param {string} num
 * @return {boolean}
 */

function is_additive(s1,s2,s3){
    if(s3.length==0)										//If we reach this condition, it means the rest of the string has been traversed and all conditions met
        return true;
    var res=(parseInt(s1)+parseInt(s2)).toString();
    if(!s3.startsWith(res))									//If the total of the first two numbers is not present at the beginning of the rest of the string
        return false;
    return is_additive(s2,res,s3.slice(res.length));
}

var isAdditiveNumber = function(num) {
    if(num.length<3)
        return false;
    
    for(var i=0;i<num.length;i++){
        for(var j=i+1;j<num.length;j++){
            var s1=num.slice(0,i+1);						//First no.
            var s2=num.slice(i+1,j+1);						//Second no.
            var s3=num.slice(j+1);							//The rest of the string

            if(s1.length>1 && s1[0]=="0")					//If the first character is 0, it wont work. But if 0 is the only character, it will. We return false
            												//instead of breaking because all possible first number will have a starting 0. 
                return false;
            if(s2.length>1 && s2[0]=="0")
                break;
            if(s3.length<s1.length || s3.length<s2.length)
                break;
            if(is_additive(s1,s2,s3))						//We start a recursive check on the rest of the string to find whether they give us additive combo or not
                return true;
        }
    }
    
    return false;											//If no combo works, we return false
};





/*
var isAdditiveNumber = function(num) {
    if(num.length<3)
        return false;
    
    var i,n=Math.trunc(num.length/3);
    function additive(idx,l,num){
        //console.log(l);
        if(l.length>=3 && l[l.length-1]!=l[l.length-2]+l[l.length-3])
            return false;
        if(idx==num.length && l[l.length-1]==l[l.length-2]+l[l.length-3])
            return true;
        
        for(i=idx+1;i<idx+n;i++){
            var l1=l.slice();
            if(i<=num.length){
                var s1=num.substring(idx,i);
                if(s1[0]=="0")
                    return false;
                l1.push(parseInt(s1));
                var a=additive(i,l1,num);
                l1.pop();
                if(a==true)
                    return true;
            }
        }

        return false;
    }
    
    return additive(0,[],num);
};
*/
