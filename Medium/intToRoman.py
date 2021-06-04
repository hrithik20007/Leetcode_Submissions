'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3
Output: "III"

Example 2:
Input: num = 4
Output: "IV"

Example 3:
Input: num = 9
Output: "IX"

Example 4:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''




class Solution:
    def intToRoman(self, num: int) -> str:
        dic={1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        
        s=""                #This string will store our answer                 
        l=list(dic.keys())  #This list will help us iterate over the dictionary keys and in turn access their values 
        i=len(l)-1          #Iterator

        while(i>=0):        #We will start traversing the dictionary keys from the last until the first element
            if (num%l[i])==0:   #This is for the last number in num and the final iteration of the while loop
                n=(num//l[i])
                s+=dic[l[i]]*n
                break
            else:
                n=(num//l[i])   #Num is divided by the largest number possible from the dictionary and the remainder then becomes the new num
                num=num%l[i]    #In case num is divided by a larger number the modulus will remain the same as num. So num will be constant for that.
                s+=dic[l[i]]*n
            i-=1

        return s

        
        
        
        '''
        This solution works but I want a faster and less-hardcoded solution
        
        
        s=""          
        dic={'1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX','10':'X','50':'L','100':'C','500':'D','1000':'M','40':'XL','90':'XC','400':'CD','900':'CM'}
        
        if str(num) in dic.keys():
            return dic[str(num)]
        
        j=0
        while num>0:
            d=int(num%10)
            n=d*(10**j)
            if str(n) in dic.keys():
                s=dic[str(n)]+s
            elif n>10 and n<40:
                n1=int(n//10)
                s=("X"*n1)+s
            elif n>50 and n<100:
                n1=int((n-50)//10)
                s="L"+"X"*n1+s
            elif n>100 and n<500:
                n1=int(n//100)
                s="C"*n1+s
            elif n>500 and n<1000:
                n1=int((n-500)//100)
                s="D"+"C"*n1+s
            else:
                n1=int(n//1000)
                s="M"*n1+s
            j+=1
            num=num/10
            
        return s
        '''
