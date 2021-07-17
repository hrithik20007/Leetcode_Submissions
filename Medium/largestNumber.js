/*
Given a list of non-negative integers nums, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Example 3:
Input: nums = [1]
Output: "1"

Example 4:
Input: nums = [10]
Output: "10"
*/



/*
Logic:
Very similar to selection sort for decreasing order. That is, the largest number comes in the front with each iteration. However, to compare and determine what
comes first, we combine the two string numbers at i-th and j-th index in the two combinations(i-1st & j-2nd   as well as  i-2nd & j-1st). If j-1st and i-2nd 
gives us a bigger number, then the numbers at i-th and j-th index are swapped.
Finally, we will get our required list. We join it and return the resultant string.
*/
/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    var z=0;
    for(var i in nums){
        nums[i]=nums[i].toString();
        if(nums[i]=='0')
            z+=1;
    }
    
    if(z==nums.length)
        return "0";
    
    for(i=0;i<nums.length-1;i++){
        for(j=i+1;j<nums.length;j++){
            var i1=parseInt(nums[i]+nums[j]);
            var i2=parseInt(nums[j]+nums[i]);
            if(i2>i1){
                var t=nums[i];
                nums[i]=nums[j];
                nums[j]=t;
            }
        }
    }
    
    return nums.join('');
};




/*
var largestNumber = function(nums) {
    function permute(nums,l,n1,ans){
        if(l.length==nums.length)
            return l.join('');

        for(var i=0;i<n1.length;i++){
            if(n1[i]==true)
                continue;
            n1[i]=true;
            l.push(nums[i]);
            
            r=permute(nums,l,n1,ans);
            if(parseInt(r)>ans)
                ans=r;
            
            n1[i]=false;
            l.pop();
        }
        return ans;
            
        }
        
        var n1=[];
        for(i=0;i<nums.length;i++)
            n1[i]=false;
        return permute(nums,[],n1,0);
};
*/



/*
var largestNumber = function(nums) {
    for(var i in nums){
        nums[i]=nums[i].toString();
    }
    
    if(nums.length==1)
        return nums[0];
    
    nums.sort((a,b)=>b[0]-a[0]);
    
    nums.sort((a,b)=>{
        if(a[0]==b[0]){
            var i=0,j=0;
            while(i<b.length-1 || j<a.length-1){
                if(b[i]==a[j]){
                    if(i!=b.length-1)
                        i+=1;
                    if(j!=a.length-1)
                        j+=1;
                    console.log(i,j);
                }
                else
                    break;
            }

            if(b[i]-a[j]<0)
                return -1;
            else
                return 1;
        }
    });
              
    return nums.join('');
};
*/
