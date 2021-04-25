'''
A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
    The area of the rectangular web page you designed must equal to the given target area.
    The width W should not be larger than the length L, which means L >= W.
    The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.

Example 1:
Input: area = 4
Output: [2,2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
'''




class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        s=int(round(sqrt(area)))

        '''
        Logic: Difference is minimum when a number is multiplied with itself to give the original no. Thus one of the no. must be less than or equal to the square 
        root of area.
        '''
        for i in range(1,s+1): 
            if area%i==0:
                c=i
        return [area//c,c]
        '''
        This is my solution and it works but I wanted a faster solution.
        
        
        l=[]
        c=sys.maxsize
        if area==1:     #I created a separate 'if' for this case because area//2 in line 43 becomes 0 in this case.
            return [1,1]
        else:
            a=area//2
            for i in range(1,a+1):
                if area%i==0:
                    j=area//i
                    l.append(i)
                    l.append(j)

            for k in range(1,len(l),2):
                diff=abs(l[k]-l[k-1])
                if c>diff:
                    c=diff
                    q=l[k]
                    r=l[k-1]

            return [max(q,r),min(q,r)]
        '''
