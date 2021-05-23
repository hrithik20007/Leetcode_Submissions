'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Example 3:
Input: dividend = 0, divisor = 1
Output: 0

Example 4:
Input: dividend = 1, divisor = 1
Output: 1
'''




class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        f=0
        if str(dividend)[0]=="-":
            f+=1
            dividend=int(str(dividend)[1:])
        if str(divisor)[0]=="-":
            f+=1
            divisor=int(str(divisor)[1:])
        i=0
        div=divisor
        if dividend<divisor:
            return 0
        if divisor==1:
            if f==1:
                if dividend==(2**31)+1:
                    return (-dividend+1)
                else:
                    return -dividend
            else:
                if dividend==(2**31):
                    return (dividend-1)
                else:
                    return dividend
        
        # Main method
        lower = 0
        while dividend > lower:
            q = 1
            d=divisor
            
			# Greedy Solution Part
            if lower + d + d <= dividend:       #We have added 'lower' here so that the control does not enter this block again after first time as d is updated again
                while lower + d + d <= dividend:
                    d += d
                    q +=q
                i += q
                lower += d
                
			# Probably 1 step away from result
            elif lower + d <= dividend:
                lower += d
                i += 1
                
            else:
                break   #When divisor+d>dividend
        
        if f==1:        #f=1 would indicate odd number of -ve signs and thus result will be -ve
            return -i
        else:
            return i




        '''
        This works but it utilises multiplication which is forbidden



        
        f=0
        if str(dividend)[0]=="-":
            f+=1
            dividend=int(str(dividend)[1:])
        if str(divisor)[0]=="-":
            f+=1
            divisor=int(str(divisor)[1:])

        i=1
        div=divisor     #Since divisor will change with iterations, so we store its value in div
        
        if dividend<divisor:
            return 0
        if divisor==1:
            if f==1:
                if dividend==(2**31)+1:
                    return (-dividend+1)
                else:
                    return -dividend
            else:
                if dividend==(2**31):
                    return (dividend-1)
                else:
                    return dividend
        
        while(divisor<=dividend):
            if divisor+div>dividend:
                break
            else:
                for j in range(10):
                    if divisor+(div*(10**j))>dividend:
                        break
                divisor+=(div*(10**(j-1)))  #We do j-1 because we break at j meaning that unsatisfies the condition 
                i+=10**(j-1)
                
        if f==1:        #f=1 would indicate odd number of -ve signs and thus result will be -ve
            return -i
        else:
            return i
        '''
